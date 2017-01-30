# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0192_auto_20170129_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='ais_legal',
            name='l16n',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
    ]
