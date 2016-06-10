# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0064_auto_20160609_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='angermanagement',
            name='angerHistory3',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_AngerHistory3', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='angerHistoryComplete3',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
