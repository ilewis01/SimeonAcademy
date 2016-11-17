# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0164_roommateevaluation'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommateevaluation',
            name='isComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
