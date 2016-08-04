# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0144_auto_20160804_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='isPending',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
