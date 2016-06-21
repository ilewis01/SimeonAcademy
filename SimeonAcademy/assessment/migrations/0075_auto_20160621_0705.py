# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0074_sapdemographics_date_of_assessment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sappsychoactive',
            old_name='client_id',
            new_name='clientID',
        ),
        migrations.RemoveField(
            model_name='sapdemographics',
            name='client',
        ),
        migrations.RemoveField(
            model_name='sapdemographics',
            name='date_of_assessment',
        ),
        migrations.AddField(
            model_name='sap',
            name='client',
            field=models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='date_of_assessment',
            field=models.DateField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sapdemographics',
            name='clientID',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
