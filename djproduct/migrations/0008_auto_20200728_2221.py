# Generated by Django 3.0.8 on 2020-07-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djproduct', '0007_auto_20200727_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.CharField(blank=True, choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=100),
        ),
    ]
