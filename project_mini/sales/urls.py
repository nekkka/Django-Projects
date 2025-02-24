from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalesOrderViewSet, InvoiceViewSet

router = DefaultRouter()
router.register(r'orders', SalesOrderViewSet)
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
