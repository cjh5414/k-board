# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_auto_20161022_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.datetime_safe.datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='page_view_count',
            field=models.IntegerField(default=0),
        ),
    ]