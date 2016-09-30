# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0154_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mheducation',
            name='collegeDegree',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
