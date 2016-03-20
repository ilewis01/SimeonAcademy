# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0023_auto_20160319_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='SapDemographics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date1', models.DateField(default=None, null=True, blank=True)),
                ('date2', models.DateField(default=None, null=True, blank=True)),
                ('date3', models.DateField(default=None, null=True, blank=True)),
                ('startTime1', models.CharField(default=None, max_length=8, null=True, blank=True)),
                ('startTime2', models.CharField(default=None, max_length=8, null=True, blank=True)),
                ('startTime3', models.CharField(default=None, max_length=8, null=True, blank=True)),
                ('problem', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('health', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('family', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('psychoactive', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('special', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('psychological', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('gambling', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('abilities', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('other', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('source1', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('relationship1', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('source2', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('relationship2', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SapPsychoactive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('drug1', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age1', models.IntegerField(default=0)),
                ('frequency1', models.IntegerField(default=0)),
                ('quantity1', models.IntegerField(default=0)),
                ('last1', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how1', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug2', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age2', models.IntegerField(default=0)),
                ('frequency2', models.IntegerField(default=0)),
                ('quantity2', models.IntegerField(default=0)),
                ('last2', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how2', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug3', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age3', models.IntegerField(default=0)),
                ('frequency3', models.IntegerField(default=0)),
                ('quantity3', models.IntegerField(default=0)),
                ('last3', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how3', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug4', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age4', models.IntegerField(default=0)),
                ('frequency4', models.IntegerField(default=0)),
                ('quantity4', models.IntegerField(default=0)),
                ('last4', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how4', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug5', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age5', models.IntegerField(default=0)),
                ('frequency5', models.IntegerField(default=0)),
                ('quantity5', models.IntegerField(default=0)),
                ('last5', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how5', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug6', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age6', models.IntegerField(default=0)),
                ('frequency6', models.IntegerField(default=0)),
                ('quantity6', models.IntegerField(default=0)),
                ('last6', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how6', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug7', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age7', models.IntegerField(default=0)),
                ('frequency7', models.IntegerField(default=0)),
                ('quantity7', models.IntegerField(default=0)),
                ('last7', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how7', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug8', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age8', models.IntegerField(default=0)),
                ('frequency8', models.IntegerField(default=0)),
                ('quantity8', models.IntegerField(default=0)),
                ('last8', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how8', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug9', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age9', models.IntegerField(default=0)),
                ('frequency9', models.IntegerField(default=0)),
                ('quantity9', models.IntegerField(default=0)),
                ('last9', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how9', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug10', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age10', models.IntegerField(default=0)),
                ('frequency10', models.IntegerField(default=0)),
                ('quantity10', models.IntegerField(default=0)),
                ('last10', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how10', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug11', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age11', models.IntegerField(default=0)),
                ('frequency11', models.IntegerField(default=0)),
                ('quantity11', models.IntegerField(default=0)),
                ('last11', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how11', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('drug12', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('age12', models.IntegerField(default=0)),
                ('frequency12', models.IntegerField(default=0)),
                ('quantity12', models.IntegerField(default=0)),
                ('last12', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('how12', models.CharField(default=None, max_length=20, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='sap',
            name='abilities',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age1',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age10',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age11',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age12',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age2',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age3',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age4',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age5',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age6',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age7',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age8',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='age9',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='client',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='date1',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='date2',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='date3',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug1',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug10',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug11',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug12',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug2',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug3',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug4',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug5',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug6',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug7',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug8',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='drug9',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='family',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency1',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency10',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency11',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency12',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency2',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency3',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency4',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency5',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency6',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency7',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency8',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='frequency9',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='gambling',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='health',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how1',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how10',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how11',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how12',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how2',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how3',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how4',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how5',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how6',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how7',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how8',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='how9',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last1',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last10',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last11',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last12',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last2',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last3',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last4',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last5',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last6',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last7',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last8',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='last9',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='other',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='psychological',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity1',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity10',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity11',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity12',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity2',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity3',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity4',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity5',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity6',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity7',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity8',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='quantity9',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='relationship1',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='relationship2',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='source1',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='source2',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='special',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='startTime1',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='startTime2',
        ),
        migrations.RemoveField(
            model_name='sap',
            name='startTime3',
        ),
        migrations.AddField(
            model_name='sap',
            name='demographics',
            field=models.ForeignKey(default=None, blank=True, to='assessment.SapDemographics', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sap',
            name='psychoactive',
            field=models.ForeignKey(default=None, blank=True, to='assessment.SapPsychoactive', null=True),
            preserve_default=True,
        ),
    ]
