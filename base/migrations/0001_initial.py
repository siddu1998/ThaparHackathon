# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 19:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desciption', models.TextField(null=True)),
                ('institute', models.TextField(null=True)),
                ('percentage', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LatestUpdates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('priority', models.CharField(choices=[('imp', 'Very Important'), ('reg', 'Regular')], max_length=3)),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('desciption', models.CharField(default='', max_length=500)),
                ('profile_image', models.FileField(blank=True, null=True, upload_to='')),
                ('user_type', models.CharField(choices=[('stu', 'Student'), ('tea', 'teacher'), ('rst', 'Reaserch Student')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.UserProfile'),
        ),
    ]