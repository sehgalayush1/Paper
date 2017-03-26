# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_story_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='services.Service'),
        ),
    ]
