# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0101_auto_20160707_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asi',
            name='endTime',
            field=models.CharField(default=None, max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asi',
            name='startTime',
            field=models.CharField(default=None, max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
    ]
