# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0030_auto_20160615_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer_ngo_request',
            name='time_vol',
            field=models.TimeField(default=datetime.datetime(2016, 6, 15, 15, 25, 12, 354000)),
        ),
    ]
