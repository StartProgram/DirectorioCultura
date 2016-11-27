# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=70)),
                ('horario', models.DateTimeField(null=True, blank=True)),
                ('descripcion', models.TextField(max_length=200)),
                ('imagen', models.ImageField(null=True, upload_to=b'img/', blank=True)),
                ('categoria', models.ForeignKey(blank=True, to='artistas.Categoria', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resenia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=35, null=True, blank=True)),
                ('contenido', models.TextField(max_length=250)),
                ('evento', models.ForeignKey(to='eventos.Evento')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
