# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0031_auto_20160321_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='A_Time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.CharField(default=None, max_length=12, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=None, null=True, blank=True)),
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(default=None, null=True, blank=True)),
                ('end', models.DateTimeField(default=None, null=True, blank=True)),
                ('bill', models.IntegerField(default=0)),
                ('appointment', models.ForeignKey(default=None, blank=True, to='assessment.Appointment', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_type', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('duration', models.IntegerField(default=0)),
                ('fee', models.IntegerField(default=0)),
                ('notes', models.CharField(default=None, max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='session',
            name='s_type',
            field=models.ManyToManyField(default=None, to='assessment.SType', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='sessionType',
            field=models.ForeignKey(default=None, blank=True, to='assessment.SType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.ForeignKey(default=None, blank=True, to='assessment.A_Time', null=True),
            preserve_default=True,
        ),
    ]
