# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='descripcion',
            field=models.TextField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artista',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'img/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artista',
            name='telefono',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
