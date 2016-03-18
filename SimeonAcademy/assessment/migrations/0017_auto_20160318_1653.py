# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0016_auto_20160318_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='angermanagement',
            name='adolescent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='anxietyExplainRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='anxietyRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='depress30ExplainRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='depress30RecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='didCompleteTreatRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='durationRecentV',
            field=models.CharField(default=None, max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='episodeEndRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='hadDrugsRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='hadDrugsRecentVExplain',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='hallucinationRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='hallucinationRecentVmos',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='hallucinationRecentVyrs',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='happenedRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='hasAttemptedExplainRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='hasAttemptedSuicide',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='homicidal',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='homicidalExplain',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='howfeelRecentV',
            field=models.CharField(default=None, max_length=8, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='intensityRecentV',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='last6Months',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='longAgoTreatRecentVmos',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='longAgoTreatRecentVyrs',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='medRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='medRecentVExplain',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='medSuccessExplainRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='medSuccessRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='onlyAsAdult',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='otherExplainRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='otherRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='physicalRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='propertyRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='psychoRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='psychoWhyRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='reasonNotCompleteRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='recentIncidentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='recentVDate',
            field=models.DateField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='recentVlocation',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='sinceChildhood',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='suicide30ExplainRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='suicide30RecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='suicideTodayExplainRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='suicideTodayPlanRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='suicideTodayRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='thisMonthOnly',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='thisTimeOnly',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='threatsRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='troubleControlExplainRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='troubleControlRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='troubleControlRecentVmos',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='troubleControlRecentVyrs',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='typeWordsRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='typicalRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='understandingExplainRecentV',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='understandingRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='verbalRecentV',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='withWhomRecentV',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='isDischarged',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='middleInit',
            field=models.CharField(default=None, max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='angermanagement',
            name='angryAbout',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='angermanagement',
            name='describeIssue',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='angermanagement',
            name='otherWhom',
            field=models.CharField(default=None, max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='angermanagement',
            name='whichMeds',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
