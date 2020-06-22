from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255,)
    email = models.EmailField(null=True, blank=True, max_length=254,)
    first_name = models.CharField(null=True, blank=True, max_length=256,)
    last_name = models.CharField(null=True, blank=True, max_length=256,)
    timestamp_created = models.DateTimeField(null=True, blank=True, auto_now_add=True,)
    last_updated = models.DateTimeField(null=True, blank=True, auto_now=True,)
    phone_number = models.CharField(null=True, blank=True, max_length=256,)
    address = models.TextField(null=True, blank=True,)
    photo = models.URLField(null=True, blank=True,)
    reviews = models.OneToOneField(
        "home.Reviews",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_reviews",
    )
    saved_items = models.OneToOneField(
        "home.Saved",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_saved_items",
    )
    recently_viewed = models.OneToOneField(
        "home.RecentlyViewed",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_recently_viewed",
    )
    listings = models.OneToOneField(
        "home.SellerListings",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_listings",
    )
    purchases = models.OneToOneField(
        "home.CustomerPurchases",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_purchases",
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
