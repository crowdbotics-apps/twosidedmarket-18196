from django.conf import settings
from django.db import models


class Review(models.Model):
    "Generated Model"
    rating = models.FloatField(null=True, blank=True,)
    description = models.CharField(null=True, blank=True, max_length=256,)
    review_title = models.CharField(null=True, blank=True, max_length=256,)
    category = models.OneToOneField(
        "item.Category",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="review_category",
    )
    reviewer = models.OneToOneField(
        "home.CustomerProfile",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="review_reviewer",
    )
    seller = models.OneToOneField(
        "home.SellerProfile",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="review_seller",
    )


class Category(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    icon = models.URLField(null=True, blank=True,)


class Item(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    category = models.OneToOneField(
        "item.Category",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="item_category",
    )
    photo = models.URLField(null=True, blank=True,)
    price = models.FloatField(null=True, blank=True,)
    condition = models.CharField(null=True, blank=True, max_length=256,)
    brand = models.CharField(null=True, blank=True, max_length=256,)
    color = models.CharField(null=True, blank=True, max_length=256,)
    quantity = models.IntegerField(null=True, blank=True,)
    shipping_price = models.FloatField(null=True, blank=True,)
    shipping_time = models.IntegerField(null=True, blank=True,)
    description = models.CharField(null=True, blank=True, max_length=256,)
    seller_profile = models.OneToOneField(
        "home.SellerProfile",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="item_seller_profile",
    )
    active = models.BooleanField(null=True, blank=True,)


# Create your models here.
