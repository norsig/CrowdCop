# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-13 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdcop_web', '0028_auto_20160413_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='When did this occur (If known, enter date and time).'),
        ),
    ]
