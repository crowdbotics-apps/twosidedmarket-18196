# Generated by Django 2.2.13 on 2020-06-18 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_auto_20200618_1815"),
        ("item", "0002_auto_20200618_1746"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="active",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="review",
            name="seller",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review_seller",
                to="home.SellerProfile",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="seller_profile",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="item_seller_profile",
                to="home.SellerProfile",
            ),
        ),
    ]
