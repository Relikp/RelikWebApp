# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-23 18:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_auto_20180423_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='wished_by',
            new_name='wisher',
        ),
    ]
