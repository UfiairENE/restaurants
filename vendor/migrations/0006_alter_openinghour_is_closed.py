# Generated by Django 4.1.2 on 2023-01-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_rename_openinghours_openinghour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghour',
            name='is_closed',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
