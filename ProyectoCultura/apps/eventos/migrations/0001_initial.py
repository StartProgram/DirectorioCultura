# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0002_auto_20161105_0211'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=70)),
                ('horario', models.DateTimeField()),
                ('descripcion', models.TextField(max_length=200)),
                ('imagen', models.ImageField(upload_to=b'/img')),
                ('categoria', models.ForeignKey(blank=True, to='artistas.Categoria', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tamanio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='evento',
            name='tamanio',
            field=models.ForeignKey(blank=True, to='eventos.Tamanio', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evento',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
