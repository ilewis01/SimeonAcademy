# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0191_auto_20170128_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='ais_family',
            name='comments',
            field=models.CharField(default=None, max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_general',
            name='comments',
            field=models.CharField(default=None, max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_drug1',
            name='comments',
            field=models.CharField(default=None, max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_employment',
            name='comments',
            field=models.CharField(default=None, max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_legal',
            name='comments',
            field=models.CharField(default=None, max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_medical',
            name='comments',
            field=models.CharField(default=None, max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_psych',
            name='comments',
            field=models.CharField(default=None, max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_social2',
            name='comments',
            field=models.CharField(default=None, max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
