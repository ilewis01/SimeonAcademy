# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0009_drug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discharge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('discharge_date', models.DateField(default=None, null=True, blank=True)),
                ('diagnosis', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('recommendations', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('treatmentNotes', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TermReason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(default=None, max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='discharge',
            name='termReason',
            field=models.ForeignKey(default=None, blank=True, to='assessment.TermReason', null=True),
            preserve_default=True,
        ),
    ]
