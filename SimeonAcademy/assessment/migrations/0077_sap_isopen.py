# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0076_auto_20160623_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='sap',
            name='isOpen',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
