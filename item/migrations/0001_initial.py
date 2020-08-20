# Generated by Django 3.0.8 on 2020-08-20 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('L1', 'Level 1'), ('L2', 'Level 2'), ('L3', 'Level 3')], max_length=2)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20)),
                ('category', models.ForeignKey(default='id', on_delete=django.db.models.deletion.CASCADE, to='item.Category')),
            ],
            options={
                'verbose_name': 'sub-category',
                'verbose_name_plural': 'sub-categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('price', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('item_level', models.CharField(default='Обычный', max_length=20)),
                ('sub_category', models.ForeignKey(default='id', on_delete=django.db.models.deletion.CASCADE, to='item.SubCategory')),
                ('tags', models.ManyToManyField(blank=True, to='item.Tag')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('item', models.ForeignKey(default='id', on_delete=django.db.models.deletion.CASCADE, to='item.Item')),
            ],
            options={
                'verbose_name': 'feedback',
                'verbose_name_plural': 'feedbacks',
            },
        ),
        migrations.CreateModel(
            name='ChangeOwnerList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_item', models.DateTimeField(blank=True, null=True)),
                ('sell_item', models.DateTimeField(blank=True, null=True)),
                ('item_id', models.ForeignKey(default='id', on_delete=django.db.models.deletion.CASCADE, to='item.Item')),
                ('user', models.ManyToManyField(blank=True, to='user.User')),
            ],
            options={
                'verbose_name': 'change owner list',
                'verbose_name_plural': 'changes owner list',
            },
        ),
    ]
