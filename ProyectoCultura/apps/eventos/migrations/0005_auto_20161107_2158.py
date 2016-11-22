# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_remove_evento_tamanio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='horario',
        ),
        migrations.AddField(
            model_name='evento',
            name='tamanio',
            field=models.ForeignKey(blank=True, to='eventos.Tamanio', null=True),
            preserve_default=True,
        ),
    ]
