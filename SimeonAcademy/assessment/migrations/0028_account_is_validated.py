# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0027_auto_20160320_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_validated',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
