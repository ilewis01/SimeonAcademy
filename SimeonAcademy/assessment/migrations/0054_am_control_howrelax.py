# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0053_am_worstepisode_whodiditfight'),
    ]

    operations = [
        migrations.AddField(
            model_name='am_control',
            name='howRelax',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
