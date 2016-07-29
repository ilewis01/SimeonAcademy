# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0142_auto_20160729_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ais_medical',
            name='m5Exp',
            field=models.CharField(default=None, max_length=22, null=True, blank=True),
            preserve_default=True,
        ),
    ]
