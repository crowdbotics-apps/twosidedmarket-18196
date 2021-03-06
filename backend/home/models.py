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


class RecentlyViewed(models.Model):
    "Generated Model"
    item = models.OneToOneField(
        "item.Item", on_delete=models.CASCADE, related_name="recentlyviewed_item",
    )


class SellerListings(models.Model):
    "Generated Model"
    listing = models.OneToOneField(
        "item.Item", on_delete=models.CASCADE, related_name="sellerlistings_listing",
    )


class CustomerPurchases(models.Model):
    "Generated Model"
    order = models.OneToOneField(
        "checkout.Order",
        on_delete=models.CASCADE,
        related_name="customerpurchases_order",
    )


class Chat(models.Model):
    "Generated Model"
    messages = models.OneToOneField(
        "home.Message",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="chat_messages",
    )
    recepient = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="chat_recepient",
    )


class Message(models.Model):
    "Generated Model"
    messageID = models.CharField(max_length=256,)
    text = models.TextField(null=True, blank=True,)


class Inbox(models.Model):
    "Generated Model"
    chats = models.OneToOneField(
        "home.Chat",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="inbox_chats",
    )
