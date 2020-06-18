from django.conf import settings
from django.db import models


class Order(models.Model):
    "Generated Model"
    item = models.OneToOneField(
        "item.Item",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="order_item",
    )
    bill = models.OneToOneField(
        "checkout.Bill",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="order_bill",
    )
    quantity = models.PositiveIntegerField(null=True, blank=True,)
    payment_method = models.OneToOneField(
        "checkout.PaymentMethod",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="order_payment_method",
    )
    customer = models.OneToOneField(
        "home.CustomerProfile",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="order_customer",
    )
    shipping_status = models.CharField(max_length=256, null=True, blank=True,)
    timestamp_created = models.DateTimeField(null=True, blank=True,)


class PaymentMethod(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    detail = models.TextField(null=True, blank=True,)


class Bill(models.Model):
    "Generated Model"
    total_amount = models.FloatField()
    customer = models.OneToOneField(
        "home.CustomerProfile",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="bill_customer",
    )
    timestamp_created = models.DateTimeField(null=True, blank=True,)


class SellerOrder(models.Model):
    "Generated Model"
    order = models.OneToOneField(
        "checkout.Order", on_delete=models.CASCADE, related_name="sellerorder_order",
    )
    timestamp_created = models.DateTimeField(null=True, blank=True,)
    seller = models.OneToOneField(
        "home.SellerProfile",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sellerorder_seller",
    )


# Create your models here.
