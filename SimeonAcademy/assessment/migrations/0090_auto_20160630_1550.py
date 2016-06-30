# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0089_auto_20160630_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='MHBackground',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('spouseAge', models.IntegerField(default=0)),
                ('spouseOccupation', models.CharField(default=None, max_length=35, null=True, blank=True)),
                ('spouseEmployer', models.CharField(default=None, max_length=35, null=True, blank=True)),
                ('spouseWorkMos', models.IntegerField(default=0)),
                ('spouseWorkYrs', models.IntegerField(default=0)),
                ('childrenMale', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('childrenFemale', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('recentMove', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('motherOccupation', models.CharField(default=None, max_length=35, null=True, blank=True)),
                ('motherJobCity', models.CharField(default=None, max_length=35, null=True, blank=True)),
                ('motherJobState', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('motherAge', models.IntegerField(default=0)),
                ('motherAgeDeath', models.IntegerField(default=0)),
                ('fatherOccupation', models.CharField(default=None, max_length=35, null=True, blank=True)),
                ('fatherJobCity', models.CharField(default=None, max_length=35, null=True, blank=True)),
                ('fatherJobState', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('fatherAge', models.IntegerField(default=0)),
                ('fatherAgeDeath', models.IntegerField(default=0)),
                ('brothers', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('sisters', models.CharField(default=None, max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='MHFamily',
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='background',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MHBackground', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='backgroundComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='backgroundPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
