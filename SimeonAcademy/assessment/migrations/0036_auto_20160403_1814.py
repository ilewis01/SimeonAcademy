# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0035_sap_psychoactive2complet'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(default=None, null=True, blank=True)),
                ('end', models.DateTimeField(default=None, null=True, blank=True)),
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('billed_to', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('date', models.DateTimeField(default=None, null=True, blank=True)),
                ('service1', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('service2', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('service3', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('service4', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('service5', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('service6', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('amount', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='clientsession',
            name='invoice',
            field=models.ForeignKey(default=None, blank=True, to='assessment.Invoice', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='s_type',
            field=models.ForeignKey(default=None, blank=True, to='assessment.SType', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stype',
            name='session_type',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
