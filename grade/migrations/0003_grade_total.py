# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0002_auto_20170413_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]