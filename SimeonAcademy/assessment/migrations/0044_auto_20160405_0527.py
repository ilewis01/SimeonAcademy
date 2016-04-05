# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0043_auto_20160405_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='am_drughistory',
            name='dateTreated',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
