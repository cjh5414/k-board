# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-11 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0021_auto_20161110_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
