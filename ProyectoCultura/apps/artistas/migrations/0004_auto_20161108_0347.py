# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0003_auto_20161108_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='categoria',
            field=models.ForeignKey(blank=True, to='artistas.Categoria', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artista',
            name='departamento',
            field=models.ForeignKey(blank=True, to='artistas.Departamento', null=True),
            preserve_default=True,
        ),
    ]
