# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0068_auto_20160614_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='am_angerhistory3',
            name='adolescent',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory3',
            name='last6Months',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory3',
            name='onlyAsAdult',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory3',
            name='sinceChildhood',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory3',
            name='thisMonthOnly',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory3',
            name='thisTimeOnly',
        ),
        migrations.AddField(
            model_name='am_angerhistory3',
            name='howOften',
            field=models.CharField(default=None, max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
    ]
