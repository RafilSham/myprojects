# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-12 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20190612_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='login',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='password',
        ),
    ]
