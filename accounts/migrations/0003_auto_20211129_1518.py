# Generated by Django 3.2.9 on 2021-11-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211126_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbooks',
            name='is_favorite',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userbooks',
            name='is_reading',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userbooks',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
