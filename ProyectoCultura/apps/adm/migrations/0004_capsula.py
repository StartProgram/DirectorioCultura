# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0003_auto_20161126_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capsula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=10)),
                ('contenido', models.TextField(max_length=255)),
                ('fecha', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
