# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0091_auto_20160630_1938'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UseTable',
            new_name='MHUseTable',
        ),
        migrations.DeleteModel(
            name='MHActivity',
        ),
        migrations.DeleteModel(
            name='MHRelationship',
        ),
        migrations.RenameField(
            model_name='mhlegalhistory',
            old_name='client_id',
            new_name='clientID',
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='psychComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='psychPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='useComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='usePriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='useTable',
            field=models.ForeignKey(default=None, blank=True, to='assessment.MHUseTable', null=True),
            preserve_default=True,
        ),
    ]
