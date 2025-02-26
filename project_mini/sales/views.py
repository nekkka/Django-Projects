from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SalesOrder, Invoice
from .serializers import SalesOrderSerializer, InvoiceSerializer
from .utils import generate_invoice_pdf
from django.shortcuts import get_object_or_404


class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        order = self.get_object()
        order.status = 'approved'
        order.save()
        return Response({'status': 'Order approved'})

    @action(detail=True, methods=['post'])
    def process(self, request, pk=None):
        order = self.get_object()
        order.status = 'processed'
        order.save()
        return Response({'status': 'Order processed'})

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    @action(detail=True, methods=['get'])
    def pdf(self, request, pk=None):
        invoice = get_object_or_404(Invoice, pk=pk)
        return generate_invoice_pdf(invoice.id)
