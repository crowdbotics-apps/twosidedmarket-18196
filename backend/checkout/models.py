from django.conf import settings
from django.db import models


class Order(models.Model):
    "Generated Model"
    item = models.OneToOneField(
        "item.Item",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="order_item",
    )
    bill = models.OneToOneField(
        "checkout.Bill",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="order_bill",
    )
    quantity = models.PositiveIntegerField(null=True, blank=True,)
    payment_method = models.OneToOneField(
        "checkout.PaymentMethod",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="order_payment_method",
    )
    shipping_status = models.CharField(null=True, blank=True, max_length=256,)
    timestamp_created = models.DateTimeField(null=True, blank=True,)
    customer = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="order_customer",
    )
    order_confirmation = models.CharField(max_length=256, null=True, blank=True,)


class PaymentMethod(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    detail = models.TextField(null=True, blank=True,)


class Bill(models.Model):
    "Generated Model"
    total_amount = models.FloatField()
    timestamp_created = models.DateTimeField(null=True, blank=True,)
    customer = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="bill_customer",
    )


class SellerOrder(models.Model):
    "Generated Model"
    order = models.OneToOneField(
        "checkout.Order", on_delete=models.CASCADE, related_name="sellerorder_order",
    )
    timestamp_created = models.DateTimeField(null=True, blank=True,)
    seller = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sellerorder_seller",
    )


# Create your models here.
