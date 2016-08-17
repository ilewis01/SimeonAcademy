# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0152_am_currentproblem_otherwhom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='am_worstepisode',
            name='threatsWorst',
        ),
    ]
