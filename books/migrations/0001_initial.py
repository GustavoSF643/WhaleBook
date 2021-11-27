# Generated by Django 3.2.9 on 2021-11-27 02:50

import books.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=255)),
                ('stars', models.IntegerField(validators=[books.models.validate_stars])),
                ('review', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
