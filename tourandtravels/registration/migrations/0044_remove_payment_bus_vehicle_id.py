# Generated by Django 4.1.2 on 2022-11-15 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0043_payment_bus_cvv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_bus',
            name='Vehicle_id',
        ),
    ]