# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0184_treatmentresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatmentresource',
            name='isHandiCap',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
