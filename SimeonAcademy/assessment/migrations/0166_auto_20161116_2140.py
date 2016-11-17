# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0165_roommateevaluation_iscomplete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='ref1_verified',
        ),
        migrations.RemoveField(
            model_name='application',
            name='ref2_verified',
        ),
        migrations.RemoveField(
            model_name='application',
            name='ref3_verified',
        ),
        migrations.AddField(
            model_name='application',
            name='isEvaluated',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
