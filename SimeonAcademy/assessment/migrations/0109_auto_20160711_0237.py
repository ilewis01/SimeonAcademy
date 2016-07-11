# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0108_auto_20160710_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asi',
            name='drug2',
        ),
        migrations.DeleteModel(
            name='AIS_Drug2',
        ),
        migrations.RemoveField(
            model_name='asi',
            name='drug2Complete',
        ),
        migrations.RemoveField(
            model_name='asi',
            name='drug2Priority',
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='comments',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d17',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d18',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d19',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d20',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d21',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d22',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d23',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d24',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d25',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d26',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d27',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d28',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d29',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d30',
            field=models.CharField(default=None, max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d31',
            field=models.CharField(default=None, max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d32',
            field=models.CharField(default=None, max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d33',
            field=models.CharField(default=None, max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d34',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d35',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
