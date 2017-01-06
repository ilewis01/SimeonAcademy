# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0181_note_clientid_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='clientID2',
            field=models.CharField(default=None, max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
