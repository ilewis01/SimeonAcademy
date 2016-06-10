# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0065_auto_20160609_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='am_childhoodhistory',
            name='traumaExplain',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
