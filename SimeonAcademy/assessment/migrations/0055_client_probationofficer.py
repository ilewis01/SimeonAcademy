# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0054_am_control_howrelax'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='probationOfficer',
            field=models.CharField(default=None, max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
    ]
