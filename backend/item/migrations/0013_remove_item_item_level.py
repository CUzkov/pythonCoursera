# Generated by Django 3.1 on 2020-10-02 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0012_item_is_for_sell'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_level',
        ),
    ]