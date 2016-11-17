# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0167_roommateevaluation_personality'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommateevaluation',
            name='hasCredit',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
