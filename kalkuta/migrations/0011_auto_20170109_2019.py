# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kalkuta', '0010_auto_20170108_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cilji',
            name='uporabnik',
        ),
        migrations.RemoveField(
            model_name='stanje',
            name='uporabnik',
        ),
        migrations.RemoveField(
            model_name='transakcija',
            name='uporabnik',
        ),
        migrations.DeleteModel(
            name='Cilji',
        ),
        migrations.DeleteModel(
            name='Stanje',
        ),
        migrations.DeleteModel(
            name='Transakcija',
        ),
    ]