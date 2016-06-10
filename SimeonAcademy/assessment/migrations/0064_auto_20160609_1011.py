# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0063_auto_20160609_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='adolescent',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='durationRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='episodeEndRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='hadDrugsRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='hadDrugsRecentVExplain',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='homicidal',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='homicidalExplain',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='intensityRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='last6Months',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='medRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='medRecentVExplain',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='medSuccessExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='medSuccessRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='onlyAsAdult',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='sinceChildhood',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='thisMonthOnly',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='thisTimeOnly',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory2',
            name='typicalRecentV',
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='adolescent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='durationRecentV',
            field=models.CharField(default=None, max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='episodeEndRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='hadDrugsRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='hadDrugsRecentVExplain',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='homicidal',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='homicidalExplain',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='intensityRecentV',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='last6Months',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='medRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='medRecentVExplain',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='medSuccessExplainRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='medSuccessRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='onlyAsAdult',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='sinceChildhood',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='thisMonthOnly',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='thisTimeOnly',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='typicalRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
