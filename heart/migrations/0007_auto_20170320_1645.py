# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 08:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0006_auto_20170320_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htem',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 20, 8, 44, 59, 607000, tzinfo=utc)),
        ),
    ]
