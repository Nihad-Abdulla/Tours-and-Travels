# Generated by Django 4.1.2 on 2022-11-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0044_remove_payment_bus_vehicle_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_bus',
            name='Total_amount',
            field=models.IntegerField(null=True),
        ),
    ]