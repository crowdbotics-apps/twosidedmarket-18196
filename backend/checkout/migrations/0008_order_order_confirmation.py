# Generated by Django 2.2.13 on 2020-06-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0007_auto_20200622_1648"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="order_confirmation",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
