# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_userprofile_current_cgpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='current_cgpa',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
