# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0107_remove_ais_employment_e5exp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ais_drug2',
            name='d14',
        ),
        migrations.RemoveField(
            model_name='ais_drug2',
            name='d15',
        ),
        migrations.RemoveField(
            model_name='ais_drug2',
            name='d16',
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d14',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d15',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d16',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
    ]
