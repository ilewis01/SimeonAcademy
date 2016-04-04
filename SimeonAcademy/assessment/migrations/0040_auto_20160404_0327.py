# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0039_auto_20160404_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='am_demographic',
            name='client',
            field=models.ForeignKey(default=None, to='assessment.Client'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='date_of_assessment',
            field=models.DateField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='drop_out',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='education',
            field=models.ForeignKey(default=None, blank=True, to='assessment.EducationLevel', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='emp_address',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='employed_months',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='employed_years',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='employee',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='employer_phone',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='job_title',
            field=models.CharField(default=None, max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='livingSituation',
            field=models.ForeignKey(default=None, blank=True, to='assessment.LivingSituation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='maritalStatus',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MaritalStatus', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='months_res',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='num_children',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='other_dependants',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='own',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='resasonDO',
            field=models.CharField(default=None, max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_demographic',
            name='years_res',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
