# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0017_auto_20160318_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='sap',
            name='startTime1',
            field=models.CharField(default=None, max_length=8, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='startTime2',
            field=models.CharField(default=None, max_length=8, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='startTime3',
            field=models.CharField(default=None, max_length=8, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='discharge',
            name='diagnosis',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
