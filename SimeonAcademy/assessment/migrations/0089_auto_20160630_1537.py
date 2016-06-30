# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0088_auto_20160628_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mheducation',
            old_name='millitaryBranch',
            new_name='militaryBranch',
        ),
        migrations.RenameField(
            model_name='mheducation',
            old_name='millitaryRank',
            new_name='militaryRank',
        ),
        migrations.RenameField(
            model_name='mheducation',
            old_name='millitaryYears',
            new_name='militaryYears',
        ),
        migrations.RemoveField(
            model_name='mheducation',
            name='wasMillitary',
        ),
        migrations.AlterField(
            model_name='mheducation',
            name='tradeSchool',
            field=models.CharField(default=None, max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
    ]
