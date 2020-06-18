from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    BillViewSet,
    OrderViewSet,
    PaymentMethodViewSet,
    SellerOrderViewSet,
)

router = DefaultRouter()
router.register("order", OrderViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("bill", BillViewSet)
router.register("sellerorder", SellerOrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
