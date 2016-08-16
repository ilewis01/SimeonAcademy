# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0151_auto_20160816_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='am_currentproblem',
            name='otherWhom',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
