# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-19 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ip',
            field=models.GenericIPAddressField(default='', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.GenericIPAddressField(default='', null=True),
        ),
    ]
