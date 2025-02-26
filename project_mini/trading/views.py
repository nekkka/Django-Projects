from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from django.utils.timezone import now
from datetime import timedelta
from rest_framework.views import APIView
from django.db.models import Sum, F
from django.http import HttpResponse
import csv



class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status != Order.PENDING:
            return Response({"error": "You can only update pending orders."}, status=400)
        return super().update(request, *args, **kwargs)

class TradingAnalyticsView(APIView):
    def get(self, request):
        today = now().date()
        last_week = today - timedelta(days=7)
        last_month = today - timedelta(days=30)

        total_volume = Order.total_trading_volume()
        total_revenue = Order.total_revenue()

        weekly_revenue = Order.objects.filter(created_at__gte=last_week).aggregate(
            revenue=Sum(F('quantity') * F('price'))
        )['revenue'] or 0

        monthly_revenue = Order.objects.filter(created_at__gte=last_month).aggregate(
            revenue=Sum(F('quantity') * F('price'))
        )['revenue'] or 0

        return Response({
            "total_volume": total_volume,
            "total_revenue": total_revenue,
            "weekly_revenue": weekly_revenue,
            "monthly_revenue": monthly_revenue,
        })



class ExportOrdersCSVView(APIView):
    def get(self, request):
    
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'
        writer = csv.writer(response)  
        writer.writerow(['ID', 'User', 'Type', 'Price', 'Quantity', 'Status', 'Created At'])



        orders = Order.objects.all()
        for order in orders:
            writer.writerow([
                order.id,
                order.user.username,
                order.order_type,
                order.price,
                order.quantity,
                order.status,
                order.created_at.strftime('%Y-%m-%d %H:%M:%S')
            ])

        return response