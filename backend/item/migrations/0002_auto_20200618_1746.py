# Generated by Django 2.2.13 on 2020-06-18 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200618_1746'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_reviewer', to='home.CustomerProfile'),
        ),
        migrations.AlterField(
            model_name='item',
            name='seller_profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_seller_profile', to='home.CustomerProfile'),
        ),
    ]