# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0026_auto_20160319_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='am_angerhistory',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='am_angertarget',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='am_childhoodhistory',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='am_connections',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='am_control',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='am_currentproblem',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='am_drughistory',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='am_familyorigin',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='am_final',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='am_worstepisode',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='clientID',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='familyhistory',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhactivity',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mheducation',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhfamily',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhlegalhistory',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhrelationship',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhstressor',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sappsychoactive',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usetable',
            name='client_id',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
