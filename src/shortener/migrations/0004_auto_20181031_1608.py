# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-10-31 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20181028_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_dot_com, shortener.validators.validate_url]),
        ),
    ]
