# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0106_auto_20160710_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ais_employment',
            name='e5Exp',
        ),
    ]
