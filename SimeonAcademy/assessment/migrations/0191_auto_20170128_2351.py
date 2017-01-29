# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0190_auto_20170126_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ais_medical',
            name='m3',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_medical',
            name='m4',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_medical',
            name='m5',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
    ]
