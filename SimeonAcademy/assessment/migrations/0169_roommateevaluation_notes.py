# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0168_roommateevaluation_hascredit'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommateevaluation',
            name='notes',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
