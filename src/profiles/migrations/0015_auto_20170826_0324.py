# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 19:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20170826_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.AddField(
            model_name='time',
            name='description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='time',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 8, 26, 3, 24, 14, 187669), verbose_name='Date'),
        ),
    ]
