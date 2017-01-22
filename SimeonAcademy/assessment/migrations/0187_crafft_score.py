# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0186_crafft'),
    ]

    operations = [
        migrations.AddField(
            model_name='crafft',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
