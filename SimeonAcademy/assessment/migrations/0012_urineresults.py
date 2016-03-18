# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0011_auto_20160318_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrineResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testDate', models.DateField(default=None, null=True, blank=True)),
                ('drug1', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug2', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug3', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug4', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug5', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug6', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug7', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug8', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug9', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug10', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug11', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug12', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
