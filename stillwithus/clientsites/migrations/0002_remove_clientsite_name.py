# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 06:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientsites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientsite',
            name='name',
        ),
    ]
