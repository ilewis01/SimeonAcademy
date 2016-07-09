# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0104_auto_20160709_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ais_medical',
            name='m10',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_medical',
            name='m11',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_medical',
            name='m3',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_medical',
            name='m4',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_medical',
            name='m5',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
