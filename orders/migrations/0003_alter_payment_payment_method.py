# Generated by Django 4.1.2 on 2023-02-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_tax_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('Paystack', 'Paystack'), ('FlutterWave', 'FlutterWave')], max_length=100),
        ),
    ]
