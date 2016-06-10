# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0058_auto_20160608_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='AM_AngerHistory2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('date_of_assessment', models.DateField(default=None, null=True, blank=True)),
                ('depress30RecentV', models.BooleanField(default=False)),
                ('depress30ExplainRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('anxietyRecentV', models.BooleanField(default=False)),
                ('anxietyExplainRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('hallucinationRecentV', models.BooleanField(default=False)),
                ('hallucinationRecentVmos', models.IntegerField(default=0)),
                ('hallucinationRecentVyrs', models.IntegerField(default=0)),
                ('understandingRecentV', models.BooleanField(default=False)),
                ('understandingExplainRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('troubleControlRecentV', models.BooleanField(default=False)),
                ('troubleControlRecentVmos', models.IntegerField(default=0)),
                ('troubleControlRecentVyrs', models.IntegerField(default=0)),
                ('troubleControlExplainRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('suicide30RecentV', models.BooleanField(default=False)),
                ('suicide30ExplainRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('suicideTodayRecentV', models.BooleanField(default=False)),
                ('suicideTodayPlanRecentV', models.BooleanField(default=False)),
                ('suicideTodayExplainRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('hasAttemptedSuicide', models.BooleanField(default=False)),
                ('hasAttemptedExplainRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('homicidal', models.BooleanField(default=False)),
                ('homicidalExplain', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('medRecentV', models.BooleanField(default=False)),
                ('medRecentVExplain', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('medSuccessRecentV', models.BooleanField(default=False)),
                ('medSuccessExplainRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('episodeEndRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('hadDrugsRecentV', models.BooleanField(default=False)),
                ('hadDrugsRecentVExplain', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('typicalRecentV', models.BooleanField(default=False)),
                ('durationRecentV', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('intensityRecentV', models.IntegerField(default=0)),
                ('thisTimeOnly', models.BooleanField(default=False)),
                ('thisMonthOnly', models.BooleanField(default=False)),
                ('last6Months', models.BooleanField(default=False)),
                ('sinceChildhood', models.BooleanField(default=False)),
                ('adolescent', models.BooleanField(default=False)),
                ('onlyAsAdult', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='adolescent',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='anxietyExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='anxietyRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='depress30ExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='depress30RecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='durationRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='episodeEndRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='hadDrugsRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='hadDrugsRecentVExplain',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='hallucinationRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='hallucinationRecentVmos',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='hallucinationRecentVyrs',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='hasAttemptedExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='hasAttemptedSuicide',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='homicidal',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='homicidalExplain',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='intensityRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='last6Months',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='medRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='medRecentVExplain',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='medSuccessExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='medSuccessRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='onlyAsAdult',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='sinceChildhood',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='suicide30ExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='suicide30RecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='suicideTodayExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='suicideTodayPlanRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='suicideTodayRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='thisMonthOnly',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='thisTimeOnly',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='troubleControlExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='troubleControlRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='troubleControlRecentVmos',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='troubleControlRecentVyrs',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='typicalRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='understandingExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='understandingRecentV',
        ),
    ]
