# Generated by Django 3.0.8 on 2020-07-27 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0004_auto_20200727_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_message',
            name='user_ip_address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]