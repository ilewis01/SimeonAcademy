# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0098_auto_20160705_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='am_demographic',
            name='education',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='am_demographic',
            name='livingSituation',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='am_demographic',
            name='maritalStatus',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
