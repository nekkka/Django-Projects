from django.urls import path
from .views import OrderListCreateView, OrderDetailView, TradingAnalyticsView, ExportOrdersCSVView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('analytics/', TradingAnalyticsView.as_view(), name='trading-analytics'),
    path('export/csv/', ExportOrdersCSVView.as_view(), name='export-orders-csv'),

]
