# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0003_grade_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='full',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='grade',
            name='score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='grade',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
