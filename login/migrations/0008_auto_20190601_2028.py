# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-01 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20190601_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='profile_img/%Y/%m/%d/'),
        ),
    ]
