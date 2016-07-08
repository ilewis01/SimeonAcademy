# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0100_auto_20160707_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='ais_general',
            name='test1',
            field=models.CharField(default=None, max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_general',
            name='test2',
            field=models.CharField(default=None, max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_general',
            name='test3',
            field=models.CharField(default=None, max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
