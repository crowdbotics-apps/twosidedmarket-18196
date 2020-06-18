# Generated by Django 2.2.13 on 2020-06-18 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('icon', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('review_title', models.CharField(blank=True, max_length=256, null=True)),
                ('category', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_category', to='item.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('photo', models.URLField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('condition', models.CharField(blank=True, max_length=256, null=True)),
                ('brand', models.CharField(blank=True, max_length=256, null=True)),
                ('color', models.CharField(blank=True, max_length=256, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('shipping_price', models.FloatField(blank=True, null=True)),
                ('shipping_time', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('category', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_category', to='item.Category')),
                ('seller_profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_seller_profile', to='home.Profile')),
            ],
        ),
    ]
