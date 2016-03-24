# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0032_auto_20160323_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='sap',
            name='SapComplete',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='demoComplet',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='finalComplete',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='preFinalComplete',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='psychoactiveComplet',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='specialComplete',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
    ]
