# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20170322_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='url',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]