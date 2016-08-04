# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('practo', '0002_auto_20160731_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_clinic',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2016, 7, 31), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor_clinic',
            name='updated_at',
            field=models.DateTimeField(default=datetime.date(2016, 7, 31), auto_now=True),
            preserve_default=False,
        ),
    ]
