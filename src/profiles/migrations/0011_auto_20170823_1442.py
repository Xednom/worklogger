# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 06:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20170823_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.Project'),
        ),
    ]