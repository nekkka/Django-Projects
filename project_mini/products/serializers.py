from rest_framework import serializers
from .models import Product, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'tags', 'image', 'created_at', 'updated_at']

    def get_discounted_price(self, obj):
        return obj.get_discounted_price()