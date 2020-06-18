from django.conf import settings
from django.db import models


class Order(models.Model):
    "Generated Model"
    item = models.OneToOneField(
        "home.CustomText", on_delete=models.CASCADE, related_name="order_item",
    )


# Create your models here.
