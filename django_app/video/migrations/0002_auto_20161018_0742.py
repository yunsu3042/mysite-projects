# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 07:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='publishedAt',
            new_name='published_date',
        ),
    ]
