# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0069_auto_20160614_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='am_angerhistory3',
            name='episodeEndRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory3',
            name='hadDrugsRecentV',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory3',
            name='hadDrugsRecentVExplain',
        ),
        migrations.RemoveField(
            model_name='am_angerhistory3',
            name='typicalRecentV',
        ),
    ]
