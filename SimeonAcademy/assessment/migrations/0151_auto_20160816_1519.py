# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0150_auto_20160814_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='am_worstepisode',
            old_name='whoDidItFight',
            new_name='whoUsed',
        ),
        migrations.RemoveField(
            model_name='am_worstepisode',
            name='iUsedWorst',
        ),
        migrations.RemoveField(
            model_name='am_worstepisode',
            name='theyUsedWorst',
        ),
    ]
