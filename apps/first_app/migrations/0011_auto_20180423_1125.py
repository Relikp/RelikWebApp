# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-23 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0010_auto_20180423_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='product',
        ),
    ]
