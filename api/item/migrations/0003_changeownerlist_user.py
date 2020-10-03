# Generated by Django 3.1 on 2020-08-24 14:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0002_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='changeownerlist',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]