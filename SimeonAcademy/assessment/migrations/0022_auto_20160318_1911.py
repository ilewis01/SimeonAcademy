# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0021_auto_20160318_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentalhealth',
            name='AcademicProblems10to12',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='AcademicProblems7to9',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='AcademicProblemsKto6',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='BehaviorProblems10to12',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='BehaviorProblems7to9',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='BehaviorProblemsKto6',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='Friendships10to12',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='Friendships7to9',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='FriendshipsKto6',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='Grades10to12',
            field=models.CharField(default=None, max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='Grades7to9',
            field=models.CharField(default=None, max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='GradesKto6',
            field=models.CharField(default=None, max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='advanceDegree',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='collegeDegree',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='collegeMajor',
            field=models.CharField(default=None, max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='collegeYears',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='credit',
            field=models.CharField(default=None, max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='debt',
            field=models.CharField(default=None, max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='healthCare',
            field=models.CharField(default=None, max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='honorableDischarge',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='income',
            field=models.CharField(default=None, max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='millitaryBranch',
            field=models.CharField(default=None, max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='millitaryRank',
            field=models.CharField(default=None, max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='millitaryYears',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='otherIncome',
            field=models.CharField(default=None, max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='residence',
            field=models.CharField(default=None, max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='tradeAreaStudy',
            field=models.CharField(default=None, max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='tradeSchool',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='wasMillitary',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
