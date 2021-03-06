# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 14:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_time_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='remarks',
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='time',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 8, 23, 22, 51, 32, 959668), verbose_name='Date'),
        ),
    ]
