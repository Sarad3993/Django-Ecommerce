# Generated by Django 3.0.8 on 2020-07-26 14:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djproduct', '0003_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='details',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
