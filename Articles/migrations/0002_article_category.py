# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-11 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[('politics', 'Oselu'), ('general', 'gbogbogbo')], max_length=30, verbose_name='Ipele'),
        ),
    ]
