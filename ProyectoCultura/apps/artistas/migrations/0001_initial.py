# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genero', models.BooleanField(default=True, choices=[(True, b'Masculino'), (False, b'Femenino')])),
                ('fecha_nacimiento', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to=b'img')),
                ('autorizado', models.BooleanField(default=False)),
                ('telefono', models.CharField(max_length=10)),
                ('descripcion', models.TextField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='artista',
            name='categoria',
            field=models.ForeignKey(blank=True, to='artistas.Categoria', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artista',
            name='departamento',
            field=models.ForeignKey(blank=True, to='artistas.Departamento', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artista',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
