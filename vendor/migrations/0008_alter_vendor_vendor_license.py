# Generated by Django 4.1.2 on 2023-02-25 10:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_alter_openinghour_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_license',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
