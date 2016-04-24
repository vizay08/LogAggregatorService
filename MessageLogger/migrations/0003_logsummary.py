# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageLogger', '0002_messagestatistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField()),
                ('clienttoken', models.CharField(max_length=6)),
                ('loglevel', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
    ]
