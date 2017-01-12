# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 12:29
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Racun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=30)),
                ('stanje', models.FloatField()),
                ('datum', models.DateTimeField(default=datetime.datetime.now)),
                ('lastnik_racuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transakcija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.BooleanField()),
                ('visina', models.FloatField()),
                ('datum', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]