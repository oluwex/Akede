# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-07 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Slug',
            new_name='slug',
        ),
    ]