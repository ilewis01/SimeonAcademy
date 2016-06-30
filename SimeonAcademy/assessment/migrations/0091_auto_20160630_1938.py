# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0090_auto_20160630_1550'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FamilyHistory',
            new_name='MHFamilyHistory',
        ),
        migrations.RenameField(
            model_name='mhbackground',
            old_name='fatherAge',
            new_name='acqNumber',
        ),
        migrations.RenameField(
            model_name='mhbackground',
            old_name='fatherAgeDeath',
            new_name='churchMonth',
        ),
        migrations.RenameField(
            model_name='mhbackground',
            old_name='motherAge',
            new_name='churchWeek',
        ),
        migrations.RenameField(
            model_name='mhbackground',
            old_name='motherAgeDeath',
            new_name='churchYear',
        ),
        migrations.RenameField(
            model_name='mhbackground',
            old_name='client_id',
            new_name='clientID',
        ),
        migrations.RenameField(
            model_name='mhbackground',
            old_name='spouseAge',
            new_name='closeFriendNumber',
        ),
        migrations.RenameField(
            model_name='mhbackground',
            old_name='spouseWorkMos',
            new_name='friendActMonth',
        ),
        migrations.RenameField(
            model_name='mhbackground',
            old_name='spouseWorkYrs',
            new_name='friendActWeek',
        ),
        migrations.RenameField(
            model_name='mhbackground',
            old_name='fatherJobCity',
            new_name='healthCare',
        ),
        migrations.RenameField(
            model_name='mhstressor',
            old_name='client_id',
            new_name='clientID',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='brothers',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='childrenFemale',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='childrenMale',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='fatherJobState',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='fatherOccupation',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='motherJobCity',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='motherJobState',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='motherOccupation',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='recentMove',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='sisters',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='spouseEmployer',
        ),
        migrations.RemoveField(
            model_name='mhbackground',
            name='spouseOccupation',
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='familyComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='familyHistory',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MHFamilyHistory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='familyPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='legalComplete',
            field=models.BooleanField(default=False),
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
            name='legalPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='stressPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='stressorComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='stressors',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MHStressor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='acqVisit',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='brothersRelationship',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='childrenRelationship',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='churchAffiliation',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='closeFriendVisit',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='credit',
            field=models.CharField(default=None, max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='debt',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='exRelationship',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='friendAct',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='income',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='interest',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='interestMonth',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='interestWeek',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='otherIncome',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='parentsRelationship',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='residence',
            field=models.CharField(default=None, max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='sistersRelationship',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='spouseRelationship',
            field=models.CharField(default=None, max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='workAct',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='workActMonth',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhbackground',
            name='workActWeek',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhstressor',
            name='abuseStressExp',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhstressor',
            name='addictionFamilyStressExp',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhstressor',
            name='deathStressExp',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhstressor',
            name='divorceStressExp',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhstressor',
            name='familyHealthStressExp',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhstressor',
            name='financialStressExp',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhstressor',
            name='medicalStressExp',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhstressor',
            name='moveStressExp',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhstressor',
            name='otherStressExp',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhstressor',
            name='violenceFamilyStressExp',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhstressor',
            name='abuseStress',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhstressor',
            name='addictionFamilyStress',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhstressor',
            name='deathStress',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhstressor',
            name='divorceStress',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhstressor',
            name='familyHealthStress',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhstressor',
            name='financialStress',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhstressor',
            name='medicalStress',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhstressor',
            name='moveStress',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhstressor',
            name='otherStress',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhstressor',
            name='violenceFamilyStress',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
