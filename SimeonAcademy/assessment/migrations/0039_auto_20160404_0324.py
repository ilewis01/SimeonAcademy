# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0038_auto_20160404_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='am_demographic',
            name='client',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='date_of_assessment',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='drop_out',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='education',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='emp_address',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='employed_months',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='employed_years',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='employer_phone',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='job_title',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='livingSituation',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='maritalStatus',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='months_res',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='num_children',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='other_dependants',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='own',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='resasonDO',
        ),
        migrations.RemoveField(
            model_name='am_demographic',
            name='years_res',
        ),
    ]
