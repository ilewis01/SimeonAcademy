# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0149_auto_20160810_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='am_demographic',
            name='drop_out',
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='spouse_dep',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
