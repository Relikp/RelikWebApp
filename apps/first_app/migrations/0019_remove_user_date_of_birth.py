# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-25 18:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0018_user_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
    ]
