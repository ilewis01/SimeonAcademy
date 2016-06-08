# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0055_client_probationofficer'),
    ]

    operations = [
        migrations.AddField(
            model_name='am_demographic',
            name='whatMedicine',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
