# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0080_auto_20160625_0057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mhdemographic',
            old_name='no_marriages',
            new_name='fatherAge',
        ),
        migrations.RemoveField(
            model_name='mhdemographic',
            name='client',
        ),
        migrations.RemoveField(
            model_name='mhdemographic',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='mhdemographic',
            name='debt',
        ),
        migrations.RemoveField(
            model_name='mhdemographic',
            name='healthCare',
        ),
        migrations.RemoveField(
            model_name='mhdemographic',
            name='income',
        ),
        migrations.RemoveField(
            model_name='mhdemographic',
            name='otherIncome',
        ),
        migrations.RemoveField(
            model_name='mhdemographic',
            name='residence',
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='bothers',
            field=models.CharField(default=None, max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='childrenFemale',
            field=models.CharField(default=None, max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='childrenMale',
            field=models.CharField(default=None, max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='clientID',
            field=models.CharField(default=None, max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='fatherAgeDeath',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='fatherCity',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='fatherLiving',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='fatherOccupation',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='fatherState',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='maritalStatus',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='motherAge',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='motherAgeDeath',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='motherCity',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='motherLiving',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='motherOccupation',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='motherState',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='numMarriages',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='recentMove',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='sisters',
            field=models.CharField(default=None, max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='spouseAge',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='spouseEmployer',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='spouseOccupation',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='spouseWorkMos',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='spouseWorkYrs',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhdemographic',
            name='pastJobs',
            field=models.CharField(default=None, max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
