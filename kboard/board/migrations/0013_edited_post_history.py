# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_auto_20161026_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditedPostHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
