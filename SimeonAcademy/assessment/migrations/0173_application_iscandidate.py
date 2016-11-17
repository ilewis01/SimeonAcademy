# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0172_application_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='isCandidate',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
