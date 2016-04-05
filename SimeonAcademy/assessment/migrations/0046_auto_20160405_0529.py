# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0045_auto_20160405_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='am_drughistory',
            name='dateTreated',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
