# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
