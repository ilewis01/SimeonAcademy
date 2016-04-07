# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0048_auto_20160406_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='am_demographic',
            name='employer_phone',
            field=models.CharField(default=None, max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
    ]
