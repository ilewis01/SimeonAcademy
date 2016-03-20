# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0022_auto_20160318_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='AM_AngerHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('recentIncidentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('recentVDate', models.DateField(default=None, null=True, blank=True)),
                ('recentVlocation', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('withWhomRecentV', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('happenedRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('physicalRecentV', models.BooleanField(default=False)),
                ('verbalRecentV', models.BooleanField(default=False)),
                ('threatsRecentV', models.BooleanField(default=False)),
                ('propertyRecentV', models.BooleanField(default=False)),
                ('otherRecentV', models.BooleanField(default=False)),
                ('otherExplainRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('typeWordsRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('howfeelRecentV', models.CharField(default=None, max_length=8, null=True, blank=True)),
                ('psychoRecentV', models.BooleanField(default=False)),
                ('psychoWhyRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('longAgoTreatRecentVmos', models.IntegerField(default=0)),
                ('longAgoTreatRecentVyrs', models.IntegerField(default=0)),
                ('didCompleteTreatRecentV', models.BooleanField(default=False)),
                ('reasonNotCompleteRecentV', models.CharField(default=None, max_length=100, null=True, blank=True)),
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
        migrations.CreateModel(
            name='AM_AngerTarget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('angryPartner', models.BooleanField(default=False)),
                ('angryParents', models.BooleanField(default=False)),
                ('angryChildren', models.BooleanField(default=False)),
                ('angryRelatives', models.BooleanField(default=False)),
                ('angryEmployer', models.BooleanField(default=False)),
                ('angryFriends', models.BooleanField(default=False)),
                ('angryOther', models.BooleanField(default=False)),
                ('otherWhom', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('angryAbout', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('seldomUpset', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AM_ChildhoodHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('raisedBy', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('momAlive', models.BooleanField(default=False)),
                ('dadAlive', models.BooleanField(default=False)),
                ('childTrama', models.BooleanField(default=False)),
                ('howLeftHome', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('num_siblings', models.IntegerField(default=0)),
                ('siblingsRelationship', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('dadClose', models.BooleanField(default=False)),
                ('dadCloseExplain', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('momClose', models.BooleanField(default=False)),
                ('momCloseExplain', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('wasAbused', models.BooleanField(default=False)),
                ('abusedBy', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('abuseImpact', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('childAnger', models.BooleanField(default=False)),
                ('childAngerExplain', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('otherChild', models.BooleanField(default=False)),
                ('otherChildExplain', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('parentViolence', models.BooleanField(default=False)),
                ('parentViolenceExplain', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('parentViolenceImpact', models.CharField(default=None, max_length=250, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AM_Connections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('angerWorse', models.BooleanField(default=False)),
                ('troubleWhenUsing', models.BooleanField(default=False)),
                ('lessAngry', models.BooleanField(default=False)),
                ('othersTellMe', models.BooleanField(default=False)),
                ('noConnection', models.BooleanField(default=False)),
                ('otherConnectionsUsing', models.BooleanField(default=False)),
                ('connectionExplain', models.CharField(default=None, max_length=250, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AM_Control',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('neverAttemptedControl', models.BooleanField(default=False)),
                ('talkToMyself', models.BooleanField(default=False)),
                ('whatSayYou', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('leaveScene', models.BooleanField(default=False)),
                ('howLongLeaveScene', models.IntegerField(default=0)),
                ('whatDoLeave', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('relax', models.BooleanField(default=False)),
                ('selfHelpGroup', models.BooleanField(default=False)),
                ('otherControlAnger', models.BooleanField(default=False)),
                ('doWhatOtherControl', models.CharField(default=None, max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AM_CurrentProblem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('brainInjury', models.BooleanField(default=False)),
                ('stroke', models.BooleanField(default=False)),
                ('epilepsy', models.BooleanField(default=False)),
                ('attentionDD', models.BooleanField(default=False)),
                ('pms', models.BooleanField(default=False)),
                ('depression', models.BooleanField(default=False)),
                ('ptsd', models.BooleanField(default=False)),
                ('otherSeriousIllness', models.BooleanField(default=False)),
                ('currentlyOnMeds', models.BooleanField(default=False)),
                ('whichMeds', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('describeIssue', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AM_Demographic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_assessment', models.DateField(default=None, null=True, blank=True)),
                ('own', models.BooleanField(default=False)),
                ('months_res', models.IntegerField(default=0)),
                ('years_res', models.IntegerField(default=0)),
                ('num_children', models.IntegerField(default=0)),
                ('other_dependants', models.IntegerField(default=0)),
                ('drop_out', models.BooleanField(default=False)),
                ('resasonDO', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('employee', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('job_title', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('emp_address', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('employed_months', models.IntegerField(default=0)),
                ('employed_years', models.IntegerField(default=0)),
                ('employer_phone', models.IntegerField(default=0)),
                ('health_problem', models.BooleanField(default=False)),
                ('medication', models.BooleanField(default=False)),
                ('health_exp', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('client', models.ForeignKey(default=None, to='assessment.Client')),
                ('education', models.ForeignKey(default=None, blank=True, to='assessment.EducationLevel', null=True)),
                ('livingSituation', models.ForeignKey(default=None, blank=True, to='assessment.LivingSituation', null=True)),
                ('maritalStatus', models.ForeignKey(default=None, blank=True, to='assessment.MaritalStatus', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AM_DrugHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('firstDrinkAge', models.IntegerField(default=0)),
                ('firstDrinkType', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('curUse', models.BooleanField(default=False)),
                ('useType', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('amtPerWeek', models.IntegerField(default=0)),
                ('useAmt', models.IntegerField(default=0)),
                ('everDrank', models.BooleanField(default=False)),
                ('timeQuit', models.IntegerField(default=0)),
                ('monthsQuit', models.IntegerField(default=0)),
                ('yearsQuit', models.IntegerField(default=0)),
                ('reasonQuit', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('DUI', models.BooleanField(default=False)),
                ('numDUI', models.IntegerField(default=0)),
                ('BALevel', models.FloatField(default=0.0)),
                ('drugTreatment', models.BooleanField(default=False)),
                ('treatmentPlace', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('dateTreated', models.DateField(default=None, null=True, blank=True)),
                ('finishedTreatment', models.BooleanField(default=False)),
                ('reasonNotFinishedTreatment', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('isClean', models.BooleanField(default=False)),
                ('relapseTrigger', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('drinkLastEpisode', models.BooleanField(default=False)),
                ('drinkRelationshipProblem', models.BooleanField(default=False)),
                ('needHelpDrugs', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AM_FamilyOrigin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('kidMomAnger', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('kidDadAnger', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('kidSiblingAnger', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('kidOtherAnger', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('learnFamilyAnger', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('suicideHistory', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AM_Final',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('anythingelse', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('changeLearn1', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('changeLearn2', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('changeLearn3', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AM_WorstEpisode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('whoWorst', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('happenedWorst', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('wordThoughtWorst', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('howStartWorst', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('howEndWorst', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('useWorst', models.BooleanField(default=False)),
                ('iUsedWorst', models.BooleanField(default=False)),
                ('theyUsedWorst', models.BooleanField(default=False)),
                ('physicalWorst', models.BooleanField(default=False)),
                ('verbalWorst', models.BooleanField(default=False)),
                ('threatsWorst', models.BooleanField(default=False)),
                ('propertyWorst', models.BooleanField(default=False)),
                ('otherWorst', models.BooleanField(default=False)),
                ('otherWorstDescription', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='BALevel',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='DUI',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='abuseImpact',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='abusedBy',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='adolescent',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='amtPerWeek',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angerWorse',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angryAbout',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angryChildren',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angryEmployer',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angryFriends',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angryOther',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angryParents',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angryPartner',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angryRelatives',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='anxietyExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='anxietyRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='anythingelse',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='attentionDD',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='brainInjury',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='changeLearn1',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='changeLearn2',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='changeLearn3',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='childAnger',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='childAngerExplain',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='childTrama',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='client',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='connectionExplain',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='curUse',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='currentlyOnMeds',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='dadAlive',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='dadClose',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='dadCloseExplain',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='dateTreated',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='date_of_assessment',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='depress30ExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='depress30RecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='depression',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='describeIssue',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='didCompleteTreatRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='doWhatOtherControl',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='drinkLastEpisode',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='drinkRelationshipProblem',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='drop_out',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='drugTreatment',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='durationRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='education',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='emp_address',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='employed_months',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='employed_years',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='employer_phone',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='epilepsy',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='episodeEndRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='everDrank',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='finishedTreatment',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='firstDrinkAge',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='firstDrinkType',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='hadDrugsRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='hadDrugsRecentVExplain',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='hallucinationRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='hallucinationRecentVmos',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='hallucinationRecentVyrs',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='happenedRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='happenedWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='hasAttemptedExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='hasAttemptedSuicide',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='health_exp',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='health_problem',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='homicidal',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='homicidalExplain',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='howEndWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='howLeftHome',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='howLongLeaveScene',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='howStartWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='howfeelRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='iUsedWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='intensityRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='isClean',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='job_title',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='kidDadAnger',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='kidMomAnger',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='kidOtherAnger',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='kidSiblingAnger',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='last6Months',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='learnFamilyAnger',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='leaveScene',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='lessAngry',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='livingSituation',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='longAgoTreatRecentVmos',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='longAgoTreatRecentVyrs',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='maritalStatus',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='medRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='medRecentVExplain',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='medSuccessExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='medSuccessRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='medication',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='momAlive',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='momClose',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='momCloseExplain',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='monthsQuit',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='months_res',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='needHelpDrugs',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='neverAttemptedControl',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='noConnection',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='numDUI',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='num_children',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='num_siblings',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='onlyAsAdult',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='otherChild',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='otherChildExplain',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='otherConnectionsUsing',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='otherControlAnger',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='otherExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='otherRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='otherSeriousIllness',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='otherWhom',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='otherWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='otherWorstDescription',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='other_dependants',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='othersTellMe',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='own',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='parentViolence',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='parentViolenceExplain',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='parentViolenceImpact',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='physicalRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='physicalWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='pms',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='propertyRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='propertyWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='psychoRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='psychoWhyRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='ptsd',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='raisedBy',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='reasonNotCompleteRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='reasonNotFinishedTreatment',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='reasonQuit',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='recentIncidentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='recentVDate',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='recentVlocation',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='relapseTrigger',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='relax',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='resasonDO',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='seldomUpset',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='selfHelpGroup',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='siblingsRelationship',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='sinceChildhood',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='stroke',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='suicide30ExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='suicide30RecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='suicideHistory',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='suicideTodayExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='suicideTodayPlanRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='suicideTodayRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='talkToMyself',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='theyUsedWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='thisMonthOnly',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='thisTimeOnly',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='threatsRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='threatsWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='timeQuit',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='treatmentPlace',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='troubleControlExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='troubleControlRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='troubleControlRecentVmos',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='troubleControlRecentVyrs',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='troubleWhenUsing',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='typeWordsRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='typicalRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='understandingExplainRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='understandingRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='useAmt',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='useType',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='useWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='verbalRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='verbalWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='wasAbused',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='whatDoLeave',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='whatSayYou',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='whichMeds',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='whoWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='withWhomRecentV',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='wordThoughtWorst',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='yearsQuit',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='years_res',
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='angerHistory',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_AngerHistory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='angerTarget',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_AngerTarget', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='childhood',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_ChildhoodHistory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='connections',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_Connections', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='control',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_Control', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='currentProblems',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_CurrentProblem', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='demographic',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_Demographic', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='drugHistory',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_DrugHistory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='familyOrigin',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_FamilyOrigin', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='final',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_Final', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='worstEpisode',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_WorstEpisode', null=True),
            preserve_default=True,
        ),
    ]
