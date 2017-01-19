# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0183_auto_20170115_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('address', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('city', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('state', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('zip_code', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('director_title', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('director_name', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('phone', models.CharField(default=None, max_length=14, null=True, blank=True)),
                ('fax', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('email', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('website', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('isDAS', models.BooleanField(default=False)),
                ('isAccredited', models.BooleanField(default=False)),
                ('type_organ', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('tpye_treat', models.CharField(default=None, max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
