# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('verificado', models.BooleanField(default=False)),
                ('artista', models.OneToOneField(to='artistas.Artista')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
