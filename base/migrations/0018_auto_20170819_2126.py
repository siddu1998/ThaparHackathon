# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 15:56
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20170819_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='current_cgpa',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
