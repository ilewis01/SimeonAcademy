# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0066_am_childhoodhistory_traumaexplain'),
    ]

    operations = [
        migrations.RenameField(
            model_name='am_childhoodhistory',
            old_name='siblingsRelationship',
            new_name='siblingsRelationshipExplain',
        ),
        migrations.AddField(
            model_name='am_childhoodhistory',
            name='siblingsClose',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
