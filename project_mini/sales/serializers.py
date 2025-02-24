from rest_framework import serializers
from .models import SalesOrder, SalesOrderItem, Invoice
from django.contrib.auth import get_user_model

User = get_user_model()

class SalesOrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = SalesOrderItem
        fields = '__all__'

class SalesOrderSerializer(serializers.ModelSerializer):
    items = SalesOrderItemSerializer(many=True)
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role="customer"))  

    class Meta:
        model = SalesOrder
        fields = '__all__'
    
    def create(self, validated_data):
        items_data = validated_data.pop('items') 
        order = SalesOrder.objects.create(**validated_data)  
        for item_data in items_data:
            SalesOrderItem.objects.create(order=order, **item_data)  
        return order


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
