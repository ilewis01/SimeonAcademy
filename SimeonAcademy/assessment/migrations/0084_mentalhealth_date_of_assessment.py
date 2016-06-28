# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0083_auto_20160627_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentalhealth',
            name='date_of_assessment',
            field=models.DateField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
