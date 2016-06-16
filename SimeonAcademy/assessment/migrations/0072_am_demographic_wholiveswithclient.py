# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0071_auto_20160615_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='am_demographic',
            name='whoLivesWithClient',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
