# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-14 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0013_auto_20160614_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='interests',
            field=models.ManyToManyField(to='Registration.NGODomains'),
        ),
    ]