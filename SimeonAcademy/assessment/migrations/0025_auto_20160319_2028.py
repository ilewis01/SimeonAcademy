# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0024_auto_20160319_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='MHActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('interestAct', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('interestWeek', models.IntegerField(default=0)),
                ('interestMonth', models.IntegerField(default=0)),
                ('friendsAct', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('friendsWeek', models.IntegerField(default=0)),
                ('friendsMonth', models.IntegerField(default=0)),
                ('workAct', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('workWeek', models.IntegerField(default=0)),
                ('workMonth', models.IntegerField(default=0)),
                ('churchAffiliation', models.CharField(default=None, max_length=40, null=True, blank=True)),
                ('churchWeek', models.IntegerField(default=0)),
                ('churchMonth', models.IntegerField(default=0)),
                ('churchYear', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MHDemographic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthplace', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('raised', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('no_marriages', models.IntegerField(default=0)),
                ('occupation', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('employer', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('employedMo', models.IntegerField(default=0)),
                ('employedYrs', models.IntegerField(default=0)),
                ('pastJobs', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('income', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('debt', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('credit', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('residence', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('healthCare', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('otherIncome', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MHEducation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('GradesKto6', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('BehaviorProblemsKto6', models.BooleanField(default=False)),
                ('AcademicProblemsKto6', models.BooleanField(default=False)),
                ('FriendshipsKto6', models.IntegerField(default=0)),
                ('Grades7to9', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('BehaviorProblems7to9', models.BooleanField(default=False)),
                ('AcademicProblems7to9', models.BooleanField(default=False)),
                ('Friendships7to9', models.IntegerField(default=0)),
                ('Grades10to12', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('BehaviorProblems10to12', models.BooleanField(default=False)),
                ('AcademicProblems10to12', models.BooleanField(default=False)),
                ('Friendships10to12', models.IntegerField(default=0)),
                ('collegeYears', models.IntegerField(default=0)),
                ('collegeDegree', models.BooleanField(default=False)),
                ('collegeMajor', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('advanceDegree', models.BooleanField(default=False)),
                ('tradeSchool', models.BooleanField(default=False)),
                ('tradeAreaStudy', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('wasMillitary', models.BooleanField(default=False)),
                ('millitaryBranch', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('millitaryYears', models.IntegerField(default=0)),
                ('millitaryRank', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('honorableDischarge', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MHFamily',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MHLegalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('num_arrest', models.IntegerField(default=0)),
                ('arrestCharges', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('num_convictions', models.IntegerField(default=0)),
                ('convictionCharges', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('num_DUI_charges', models.IntegerField(default=0)),
                ('num_DUI_convictions', models.IntegerField(default=0)),
                ('probationPresent', models.BooleanField(default=False)),
                ('probationPast', models.BooleanField(default=False)),
                ('probationOfficer', models.CharField(default=None, max_length=35, null=True, blank=True)),
                ('probationOffense', models.CharField(default=None, max_length=35, null=True, blank=True)),
                ('suspendedDrivePresent', models.BooleanField(default=False)),
                ('num_suspended', models.IntegerField(default=0)),
                ('hasLawsuit', models.BooleanField(default=False)),
                ('lawsuitStress', models.BooleanField(default=False)),
                ('inDivorce', models.BooleanField(default=False)),
                ('childCustody', models.BooleanField(default=False)),
                ('hasBankrupcy', models.BooleanField(default=False)),
                ('dateBenkrupcy', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('explainPositiveAnswers', models.CharField(default=None, max_length=250, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MHRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('spouseR', models.CharField(default=None, max_length=7, null=True, blank=True)),
                ('bothersR', models.CharField(default=None, max_length=7, null=True, blank=True)),
                ('childrenR', models.CharField(default=None, max_length=7, null=True, blank=True)),
                ('parentsR', models.CharField(default=None, max_length=7, null=True, blank=True)),
                ('sistersR', models.CharField(default=None, max_length=7, null=True, blank=True)),
                ('exR', models.CharField(default=None, max_length=7, null=True, blank=True)),
                ('friendsCallNum', models.IntegerField(default=0)),
                ('friendsVisitWeek', models.IntegerField(default=0)),
                ('friendsVisitMonth', models.IntegerField(default=0)),
                ('friendsVisitYear', models.IntegerField(default=0)),
                ('aquaintCallNum', models.IntegerField(default=0)),
                ('aquaintVisitWeek', models.IntegerField(default=0)),
                ('aquaintVisitMonth', models.IntegerField(default=0)),
                ('aquaintVisitYear', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MHStressor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('deathStress', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('divorceStress', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('moveStress', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('medicalStress', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('familyHealthStress', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('financialStress', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('abuseStress', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('addictionFamilyStress', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('violenceFamilyStress', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('otherStress', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('psychiatricHistory', models.CharField(default=None, max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='mentalhealth',
            old_name='drug_alcohol_use',
            new_name='useTable',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='AcademicProblems10to12',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='AcademicProblems7to9',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='AcademicProblemsKto6',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='BehaviorProblems10to12',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='BehaviorProblems7to9',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='BehaviorProblemsKto6',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='Friendships10to12',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='Friendships7to9',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='FriendshipsKto6',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='Grades10to12',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='Grades7to9',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='GradesKto6',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='abuseStress',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='addictionFamilyStress',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='advanceDegree',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='aquaintCallNum',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='aquaintVisitMonth',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='aquaintVisitWeek',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='aquaintVisitYear',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='arrestCharges',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='birthplace',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='bothersR',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='childCustody',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='childrenR',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='churchAffiliation',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='churchMonth',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='churchWeek',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='churchYear',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='client',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='collegeDegree',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='collegeMajor',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='collegeYears',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='convictionCharges',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='dateBenkrupcy',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='deathStress',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='debt',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='divorceStress',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='employedMo',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='employedYrs',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='employer',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='exR',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='explainPositiveAnswers',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='familyHealthStress',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='financialStress',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='friendsAct',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='friendsCallNum',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='friendsMonth',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='friendsVisitMonth',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='friendsVisitWeek',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='friendsVisitYear',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='friendsWeek',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='hasBankrupcy',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='hasLawsuit',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='healthCare',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='honorableDischarge',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='inDivorce',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='income',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='interestAct',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='interestMonth',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='interestWeek',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='lawsuitStress',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='medicalStress',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='millitaryBranch',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='millitaryRank',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='millitaryYears',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='moveStress',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='no_marriages',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='num_DUI_charges',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='num_DUI_convictions',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='num_arrest',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='num_convictions',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='num_suspended',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='otherIncome',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='otherStress',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='parentsR',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='pastJobs',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='probationOffense',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='probationOfficer',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='probationPast',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='probationPresent',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='psychiatricHistory',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='raised',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='sistersR',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='spouseR',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='suspendedDrivePresent',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='tradeAreaStudy',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='tradeSchool',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='violenceFamilyStress',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='wasMillitary',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='workAct',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='workMonth',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='workWeek',
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='activities',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MHActivity', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='demographics',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MHDemographic', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='education',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MHEducation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='family',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MHFamily', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='legalHistory',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MHLegalHistory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='relationships',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MHRelationship', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='stressors',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MHStressor', null=True),
            preserve_default=True,
        ),
    ]
