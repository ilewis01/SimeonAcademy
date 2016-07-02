# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0093_auto_20160701_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mhfamilyhistory',
            old_name='client_id',
            new_name='clientID',
        ),
    ]
