# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0173_application_iscandidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='isRated',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
