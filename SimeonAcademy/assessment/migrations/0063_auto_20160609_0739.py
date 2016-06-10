# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0062_auto_20160609_0656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='am_angerhistory2',
            old_name='troubleControlExplainRecentV',
            new_name='controlTrigger',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='troubleControlRecentVmos',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='troubleControlRecentVyrs',
        ),
        migrations.AddField(
            model_name='am_angerhistory2',
            name='lastTimeTroubleControl',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
