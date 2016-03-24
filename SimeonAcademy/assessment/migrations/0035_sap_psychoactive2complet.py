# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0034_auto_20160323_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='sap',
            name='psychoactive2Complet',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
