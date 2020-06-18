from rest_framework import authentication
from checkout.models import Bill, Order, PaymentMethod, SellerOrder
from .serializers import (
    BillSerializer,
    OrderSerializer,
    PaymentMethodSerializer,
    SellerOrderSerializer,
)
from rest_framework import viewsets


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Order.objects.all()


class PaymentMethodViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PaymentMethod.objects.all()


class BillViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Bill.objects.all()


class SellerOrderViewSet(viewsets.ModelViewSet):
    serializer_class = SellerOrderSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = SellerOrder.objects.all()
