# Generated by Django 3.0.8 on 2020-08-09 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0005_contact_message_user_ip_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='references',
        ),
        migrations.RemoveField(
            model_name='information',
            name='smtpemail',
        ),
        migrations.RemoveField(
            model_name='information',
            name='smtppassword',
        ),
        migrations.RemoveField(
            model_name='information',
            name='smtpport',
        ),
        migrations.RemoveField(
            model_name='information',
            name='smtpserver',
        ),
    ]