from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'order_type', 'price', 'quantity', 'status', 'created_at']
        read_only_fields = ['id', 'user', 'status', 'created_at']
