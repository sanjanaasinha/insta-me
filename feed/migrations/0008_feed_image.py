# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-24 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_remove_feed_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
