# Generated by Django 3.0.8 on 2020-08-14 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djproduct', '0028_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='djproduct.Cart'),
        ),
    ]