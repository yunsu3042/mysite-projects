# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 06:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_add'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment_Add',
            new_name='Comment',
        ),
    ]
