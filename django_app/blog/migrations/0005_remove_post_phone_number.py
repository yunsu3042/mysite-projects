# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 14:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='phone_number',
        ),
    ]
