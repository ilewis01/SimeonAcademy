# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0040_auto_20160404_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='am_drughistory',
            name='amtPerWeek',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
