# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-07 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0005_auto_20161106_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('oselu', 'Oselu'), ('gbogbogbo', 'Gbogbogbo'), ('owo', 'Owo')], max_length=30, verbose_name='Ipele'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(help_text='Type the content of your article here', max_length=1000, null=True, verbose_name='Oro Iroyin'),
        ),
    ]