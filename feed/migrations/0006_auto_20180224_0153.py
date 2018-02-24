# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-23 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import feed.models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_remove_feed_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feed',
            name='description',
            field=models.CharField(max_length=255, validators=[feed.models.validate_description]),
        ),
    ]
