# Generated by Django 4.1.2 on 2022-10-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_bus_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='busname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bus',
            name='price',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
