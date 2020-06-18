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
    last_updated = models.DateTimeField(auto_now=True, null=True, blank=True,)


class SellerProfile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="sellerprofile_user",
    )
    photo = models.URLField(null=True, blank=True,)
    timestamp_created = models.DateTimeField(auto_now=True, null=True, blank=True,)
    last_updated = models.DateTimeField(auto_now=True, null=True, blank=True,)
    reviews = models.OneToOneField(
        "item.Review",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sellerprofile_reviews",
    )


class CustomerProfile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="customerprofile_user",
    )
    photo = models.URLField(null=True, blank=True,)
    timestamp_created = models.DateTimeField(auto_now=True, null=True, blank=True,)
    last_updated = models.DateTimeField(auto_now=True, null=True, blank=True,)
