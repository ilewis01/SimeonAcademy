# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0042_auto_20160405_0509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='am_drughistory',
            name='timeQuit',
        ),
        migrations.AlterField(
            model_name='am_drughistory',
            name='BALevel',
            field=models.CharField(default=None, max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
