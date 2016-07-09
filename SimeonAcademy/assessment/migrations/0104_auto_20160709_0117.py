# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0103_auto_20160709_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discharge',
            old_name='discharge_date',
            new_name='date_of_assessment',
        ),
        migrations.RemoveField(
            model_name='discharge',
            name='termReason',
        ),
        migrations.RemoveField(
            model_name='discharge',
            name='treatmentNotes',
        ),
        migrations.AddField(
            model_name='discharge',
            name='clientAttitude',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discharge',
            name='isComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discharge',
            name='isOpen',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discharge',
            name='reasonRefered',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discharge',
            name='reasonTerminated',
            field=models.CharField(default=None, max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='discharge',
            name='diagnosis',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='discharge',
            name='recommendations',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
