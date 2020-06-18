from rest_framework import serializers
from checkout.models import Bill, Order, PaymentMethod, SellerOrder


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"


class SellerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerOrder
        fields = "__all__"
