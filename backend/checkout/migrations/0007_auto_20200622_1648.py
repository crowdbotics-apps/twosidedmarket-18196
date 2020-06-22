# Generated by Django 2.2.13 on 2020-06-22 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0006_auto_20200622_1624"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sellerorder",
            name="seller",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sellerorder_seller",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
