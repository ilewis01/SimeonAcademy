# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0118_auto_20160715_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsession',
            name='am',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AngerManagement', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='asi',
            field=models.ForeignKey(default=None, blank=True, to='assessment.ASI', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='hasAM',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='hasASI',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='hasMH',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='hasSAP',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='hasUT',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='mh',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MentalHealth', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='sap',
            field=models.ForeignKey(default=None, blank=True, to='assessment.SAP', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='ut',
            field=models.ForeignKey(default=None, blank=True, to='assessment.UrineResults', null=True),
            preserve_default=True,
        ),
    ]
