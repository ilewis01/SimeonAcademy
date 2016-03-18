# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0004_auto_20160317_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('drop_out', models.BooleanField(default=False)),
                ('reasonDO', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('level', models.CharField(default=None, max_length=35, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='date_of_assessment',
            field=models.DateField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='education',
            field=models.ForeignKey(default=None, blank=True, to='assessment.Education', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='livingSituation',
            field=models.ForeignKey(default=None, blank=True, to='assessment.LivingSituation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='maritalStatus',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MaritalStatus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='months_res',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='num_children',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='other_dependants',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='own',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='years_res',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
