from django.conf import settings
from django.db import models


class Review(models.Model):
    "Generated Model"
    rating = models.FloatField(null=True, blank=True,)
    description = models.CharField(max_length=256, null=True, blank=True,)
    review_title = models.CharField(max_length=256, null=True, blank=True,)
    category = models.OneToOneField(
        "item.Category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="review_category",
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
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="item_category",
    )
    photo = models.URLField(null=True, blank=True,)
    price = models.FloatField(null=True, blank=True,)
    condition = models.CharField(max_length=256, null=True, blank=True,)
    brand = models.CharField(max_length=256, null=True, blank=True,)
    color = models.CharField(max_length=256, null=True, blank=True,)
    quantity = models.IntegerField(null=True, blank=True,)
    shipping_price = models.FloatField(null=True, blank=True,)
    shipping_time = models.IntegerField(null=True, blank=True,)
    description = models.CharField(max_length=256, null=True, blank=True,)
    seller_profile = models.OneToOneField(
        "home.Profile",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="item_seller_profile",
    )


# Create your models here.
