# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-12 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20190601_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='login',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]