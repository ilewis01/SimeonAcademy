# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0082_auto_20160627_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentalhealth',
            old_name='activitiesComplete',
            new_name='demoPriority',
        ),
        migrations.RenameField(
            model_name='mentalhealth',
            old_name='familyComplete',
            new_name='educationPriority',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='family',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='familyHistory',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='familyHistoryComplete',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='legalHistory',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='legalHistoryComplete',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='relationships',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='relationshipsComplete',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='stressors',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='stressorsComplete',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='useTable',
        ),
        migrations.RemoveField(
            model_name='mentalhealth',
            name='useTableComplete',
        ),
    ]
