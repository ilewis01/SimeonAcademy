# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('lname', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('street_no', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('street_name', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('apartment_no', models.CharField(default=None, max_length=5, null=True, blank=True)),
                ('city', models.CharField(default=None, max_length=15, null=True, blank=True)),
                ('zip_code', models.IntegerField(default=0)),
                ('ss_num', models.CharField(default=None, max_length=11, null=True, blank=True)),
                ('dob', models.DateField(default=None, null=True, blank=True)),
                ('intake_date', models.DateField(default=None, null=True, blank=True)),
                ('em_contact_name', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('phone', models.CharField(default=None, max_length=14, null=True, blank=True)),
                ('em_phone', models.CharField(default=None, max_length=14, null=True, blank=True)),
                ('email', models.EmailField(default=None, max_length=75, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RefReason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(default=None, max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(default=None, max_length=2, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='client',
            name='reason_ref',
            field=models.ForeignKey(default=None, blank=True, to='assessment.RefReason', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='state',
            field=models.ForeignKey(default=None, blank=True, to='assessment.State', null=True),
            preserve_default=True,
        ),
    ]
