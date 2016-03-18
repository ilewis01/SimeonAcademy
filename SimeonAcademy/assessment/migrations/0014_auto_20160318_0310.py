# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0013_clinical'),
    ]

    operations = [
        migrations.CreateModel(
            name='SAP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date1', models.DateField(default=None, null=True, blank=True)),
                ('date2', models.DateField(default=None, null=True, blank=True)),
                ('date3', models.DateField(default=None, null=True, blank=True)),
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
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='clinical',
            name='client',
        ),
        migrations.DeleteModel(
            name='Clinical',
        ),
    ]
