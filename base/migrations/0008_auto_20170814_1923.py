# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20170814_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_year',
            field=models.CharField(choices=[('1st', '1st Year Student'), ('2nd', '2nd Year Student'), ('3rd', 'Third Year Student'), ('4th', '4th Year Student'), ('master', 'M.Tech Student')], default='1st', max_length=3),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('btec', 'B.TECH'), ('mtec', 'M.TECH'), ('tea', 'teacher'), ('rst', 'Reaserch Student')], max_length=3),
        ),
    ]