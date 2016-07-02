# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0092_auto_20160630_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mhfamilyhistory',
            old_name='LD',
            new_name='add',
        ),
        migrations.RenameField(
            model_name='mhfamilyhistory',
            old_name='depression',
            new_name='depressed',
        ),
        migrations.RenameField(
            model_name='mhfamilyhistory',
            old_name='hyperactivity',
            new_name='ld',
        ),
        migrations.RenameField(
            model_name='mhusetable',
            old_name='client_id',
            new_name='clientID',
        ),
        migrations.AddField(
            model_name='mheducation',
            name='military',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mheducation',
            name='tradeSch',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
