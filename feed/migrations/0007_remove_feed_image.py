# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-24 07:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_auto_20180224_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='image',
        ),
    ]
