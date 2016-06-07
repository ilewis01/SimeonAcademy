# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0052_auto_20160606_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='am_worstepisode',
            name='whoDidItFight',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
