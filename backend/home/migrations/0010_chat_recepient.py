# Generated by Django 2.2.13 on 2020-06-22 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0009_auto_20200622_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='recepient',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_recepient', to=settings.AUTH_USER_MODEL),
        ),
    ]
