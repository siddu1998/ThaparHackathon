# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicdetail',
            name='entering',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='leaving',
            field=models.DateField(null=True),
        ),
    ]
