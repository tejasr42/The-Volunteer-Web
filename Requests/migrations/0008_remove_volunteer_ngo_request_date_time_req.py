# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 05:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0007_volunteer_ngo_request_date_time_req'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer_ngo_request',
            name='date_time_req',
        ),
    ]
