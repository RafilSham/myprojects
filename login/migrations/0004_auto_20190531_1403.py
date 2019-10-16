# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20190529_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dnevnik',
            old_name='comment',
            new_name='comment1',
        ),
        migrations.RemoveField(
            model_name='dnevnik',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='dnevnik',
            name='value',
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='comment2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='comment3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='comment4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='comment5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='comment6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='comment7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='comment8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='value1',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='value2',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='value3',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='value4',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='value5',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='value6',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='value7',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='value8',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]