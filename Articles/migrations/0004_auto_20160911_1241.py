# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-11 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0003_auto_20160911_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('politics', 'Oselu'), ('general', 'Gbogbogbo')], max_length=30, verbose_name='Ipele'),
        ),
    ]
