from rest_framework import serializers
from shopping.models import Customer, Order, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)  # depth = 1

    class Meta:
        model = Order
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    payment_methods = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='payment_name'
    )
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
