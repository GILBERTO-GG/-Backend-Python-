# Generated by Django 4.2.1 on 2024-02-11 02:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("MyEcommerceApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="productmodel",
            name="color",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productmodel",
            name="description",
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productmodel",
            name="product_dimensions",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productmodel",
            name="seller",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
