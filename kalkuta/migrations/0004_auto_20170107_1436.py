# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkuta', '0003_cilji_stanje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cilji',
            name='datum',
        ),
        migrations.AddField(
            model_name='cilji',
            name='uspesnost',
            field=models.IntegerField(default=-1),
        ),
    ]
