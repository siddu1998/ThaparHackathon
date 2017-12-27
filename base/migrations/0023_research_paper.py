# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 14:22
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0022_auto_20170819_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research_Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('year', models.CharField(max_length=4)),
                ('impact_factor', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
