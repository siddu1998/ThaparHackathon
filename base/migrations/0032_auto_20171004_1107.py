# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_auto_20171004_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='How_is_the_pace_of_the_class',
            field=models.CharField(choices=[('Fast', 'Fast'), ('Perfect', 'Perfect'), ('Slow', 'Slow')], default='D', max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Planned_to_communicate_why_learning_this_is_important',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Sometimes', 'Sometimes'), ('NA', 'NA')], default='D', max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Presents_material_in_a_variety_of_ways',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Sometimes', 'Sometimes'), ('NA', 'NA')], default='D', max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='The_information_was_presented_logically',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Sometimes', 'Sometimes'), ('NA', 'NA')], default='D', max_length=10),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Were_notes_efficient_for_after_learning',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Sometimes', 'Sometimes'), ('NA', 'NA')], default='D', max_length=10),
        ),
    ]
