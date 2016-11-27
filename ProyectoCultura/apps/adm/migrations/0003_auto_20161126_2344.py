# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0002_evento_autorizado'),
        ('adm', '0002_auto_20161126_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificacionBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('verificado', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NotificacionArtista',
            fields=[
                ('notificacionbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='adm.NotificacionBase')),
                ('artista', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=('adm.notificacionbase',),
        ),
        migrations.CreateModel(
            name='NotificacionEvento',
            fields=[
                ('notificacionbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='adm.NotificacionBase')),
                ('evento', models.OneToOneField(to='eventos.Evento')),
            ],
            options={
            },
            bases=('adm.notificacionbase',),
        ),
        migrations.RemoveField(
            model_name='notificacion',
            name='artista',
        ),
        migrations.DeleteModel(
            name='Notificacion',
        ),
    ]
