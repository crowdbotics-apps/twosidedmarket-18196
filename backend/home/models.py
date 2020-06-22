from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Profile(models.Model):
    "Generated Model"
    photo = models.URLField(null=True, blank=True,)
    timestamp_created = models.DateTimeField(null=True, blank=True,)
    last_updated = models.DateTimeField(null=True, blank=True, auto_now=True,)


class SellerProfile(models.Model):
    "Generated Model"
    last_updated = models.DateTimeField(null=True, blank=True, auto_now=True,)


class CustomerProfile(models.Model):
    "Generated Model"
    photo = models.URLField(null=True, blank=True,)
    timestamp_created = models.DateTimeField(null=True, blank=True, auto_now=True,)
    last_updated = models.DateTimeField(null=True, blank=True, auto_now=True,)
    address = models.TextField(null=True, blank=True, max_length=256,)


class Favorites(models.Model):
    "Generated Model"
    test = models.BigIntegerField(null=True, blank=True,)


class Reviews(models.Model):
    "Generated Model"
    review = models.OneToOneField(
        "item.Review", on_delete=models.CASCADE, related_name="reviews_review",
    )


class Saved(models.Model):
    "Generated Model"
    item = models.OneToOneField(
        "item.Item", on_delete=models.CASCADE, related_name="saved_item",
    )
