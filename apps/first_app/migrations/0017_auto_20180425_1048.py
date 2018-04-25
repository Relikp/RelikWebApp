# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-25 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0016_auto_20180423_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='item',
            name='wisher',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='alias',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='item',
        ),
        migrations.AddField(
            model_name='quote',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_quote', to='first_app.user'),
        ),
        migrations.AddField(
            model_name='quote',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_quotes', to='first_app.user'),
        ),
    ]
