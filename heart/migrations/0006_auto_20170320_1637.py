# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0005_htem_ctime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htem',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]