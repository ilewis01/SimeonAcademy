# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0006_auto_20160318_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='em_contact_name',
            new_name='emer_contact_name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='em_phone',
            new_name='emer_phone',
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='drop_out',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='emp_address',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='employed_months',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='employed_years',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='employee',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='employer_phone',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='health_exp',
            field=models.CharField(default=None, max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='health_problem',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='job_title',
            field=models.CharField(default=None, max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='medication',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='resasonDO',
            field=models.CharField(default=None, max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
