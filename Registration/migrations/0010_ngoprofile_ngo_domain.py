# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-14 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0009_remove_ngodomains_ngo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngoprofile',
            name='ngo_domain',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
