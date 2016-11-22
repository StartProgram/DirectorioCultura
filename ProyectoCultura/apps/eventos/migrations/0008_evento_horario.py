# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0007_auto_20161108_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='horario',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
