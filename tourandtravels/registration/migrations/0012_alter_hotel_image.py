# Generated by Django 4.1.2 on 2022-10-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_alter_tourpackages_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]