# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0028_account_is_validated'),
    ]

    operations = [
        migrations.AddField(
            model_name='angermanagement',
            name='angerHistoryComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='angerTargetComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='childhoodComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='connectionsComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='controlComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='currentProblemsComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='demographicComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='drugHistoryComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='familyOriginComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='finalComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='worstComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
