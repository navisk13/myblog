# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20170608_1352'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Songs',
            new_name='Song',
        ),
    ]
