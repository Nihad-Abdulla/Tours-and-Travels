# Generated by Django 4.1.2 on 2022-11-16 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0045_alter_payment_bus_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_booking',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.login'),
        ),
    ]
