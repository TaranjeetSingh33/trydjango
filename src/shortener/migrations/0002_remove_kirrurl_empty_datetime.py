# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-10-28 05:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kirrurl',
            name='empty_datetime',
        ),
    ]
