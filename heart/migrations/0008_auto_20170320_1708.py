# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 09:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0007_auto_20170320_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htem',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 20, 9, 8, 11, 151000, tzinfo=utc)),
        ),
    ]