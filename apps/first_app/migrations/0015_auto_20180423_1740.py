# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-24 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0014_wishlist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='item',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.AddField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='first_app.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='wisher',
            field=models.ManyToManyField(related_name='wished_items', to='first_app.user'),
        ),
        migrations.DeleteModel(
            name='wishlist',
        ),
    ]
