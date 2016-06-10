# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0061_am_angerhistory3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='hallucinationRecentVmos',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='hallucinationRecentVyrs',
        ),
        migrations.AddField(
            model_name='am_angerhistory2',
            name='hallucinationLastV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
