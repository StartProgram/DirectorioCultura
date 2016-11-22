# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20161105_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='horario',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, blank=True),
            preserve_default=True,
        ),
    ]
