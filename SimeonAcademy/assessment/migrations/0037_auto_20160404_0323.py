# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0036_auto_20160403_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='angermanagement',
            name='angerHistory',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angerHistoryComplete',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angerTarget',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='angerTargetComplete',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='childhood',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='childhoodComplete',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='connections',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='connectionsComplete',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='control',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='controlComplete',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='currentProblems',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='currentProblemsComplete',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='demographic',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='demographicComplete',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='drugHistory',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='drugHistoryComplete',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='familyOrigin',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='familyOriginComplete',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='final',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='finalComplete',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='worstComplete',
        ),
        migrations.RemoveField(
            model_name='angermanagement',
            name='worstEpisode',
        ),
    ]
