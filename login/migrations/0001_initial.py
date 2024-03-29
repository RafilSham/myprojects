# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-28 15:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import login.myFields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('char_class', models.CharField(max_length=4, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'clas',
            },
        ),
        migrations.CreateModel(
            name='Dnevnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('value', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dnevnik',
            },
        ),
        migrations.CreateModel(
            name='Hw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Clas')),
            ],
            options={
                'db_table': 'hw',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Clas')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Rasp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'rasp',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_day', models.DateField()),
                ('end_day', models.DateField()),
                ('date', login.myFields.DayOfTheWeekField(choices=[('1', 'Понедельник'), ('2', 'Вторник'), ('3', 'Среда'), ('4', 'Четверг'), ('5', 'Пятница')], max_length=1)),
                ('_s1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rasp_s1', to='login.Rasp')),
                ('_s2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasp_s2', to='login.Rasp')),
                ('_s3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rasp_s3', to='login.Rasp')),
                ('_s4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasp_s4', to='login.Rasp')),
                ('_s5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rasp_s5', to='login.Rasp')),
                ('_s6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasp_s6', to='login.Rasp')),
                ('_s7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rasp_s7', to='login.Rasp')),
                ('_s8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasp_s8', to='login.Rasp')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Clas')),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('sname', models.CharField(max_length=100)),
                ('thname', models.CharField(max_length=100)),
                ('staj', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.AddField(
            model_name='rasp',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Subject'),
        ),
        migrations.AddField(
            model_name='rasp',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Teacher'),
        ),
        migrations.AddField(
            model_name='hw',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Rasp'),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Profile'),
        ),
        migrations.AddField(
            model_name='dnevnik',
            name='subject',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='login.Rasp'),
        ),
        migrations.AddField(
            model_name='clas',
            name='classmaster',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.Teacher'),
        ),
    ]
