from django.db import models
from django.conf import settings
from django.db.models import Sum, F

class Order(models.Model):
    BUY = 'BUY'
    SELL = 'SELL'

    ORDER_TYPES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]

    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=4, choices=ORDER_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.order_type} | {self.quantity} @ {self.price}"

    @staticmethod
    def total_trading_volume():
        return Order.objects.aggregate(volume=Sum('quantity'))['volume'] or 0

    @staticmethod
    def total_revenue():
        return Order.objects.aggregate(revenue=Sum(F('quantity') * F('price')))['revenue'] or 0
