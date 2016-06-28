# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0081_auto_20160627_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mheducation',
            old_name='client_id',
            new_name='clientID',
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='numBrothers',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='numChildren',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mhdemographic',
            name='numSisters',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
