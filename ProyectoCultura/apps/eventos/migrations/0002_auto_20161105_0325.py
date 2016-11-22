# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'/img', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
