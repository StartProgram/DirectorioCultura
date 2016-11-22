# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20161106_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='tamanio',
        ),
    ]
