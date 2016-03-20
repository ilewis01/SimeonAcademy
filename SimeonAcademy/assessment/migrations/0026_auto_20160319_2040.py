# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0025_auto_20160319_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='mhfamily',
            name='brothers',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='childrenFemale',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='childrenMale',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='fatherAge',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='fatherAgeDeath',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='fatherJobCity',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='fatherJobState',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='fatherOccupation',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='motherAge',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='motherAgeDeath',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='motherJobCity',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='motherJobState',
            field=models.CharField(default=None, max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='motherOccupation',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='recentMove',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='sisters',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='spouseAge',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='spouseEmployer',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='spouseOccupation',
            field=models.CharField(default=None, max_length=35, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='spouseWorkMos',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhfamily',
            name='spouseWorkYrs',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
