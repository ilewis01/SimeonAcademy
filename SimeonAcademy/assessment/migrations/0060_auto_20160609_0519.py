# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0059_auto_20160609_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='angermanagement',
            name='angerHistory2',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_AngerHistory2', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='angerHistoryComplete2',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
