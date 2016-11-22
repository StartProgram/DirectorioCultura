# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0002_auto_20161105_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='categoria',
            field=models.OneToOneField(null=True, blank=True, to='artistas.Categoria'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artista',
            name='departamento',
            field=models.OneToOneField(null=True, blank=True, to='artistas.Departamento'),
            preserve_default=True,
        ),
    ]
