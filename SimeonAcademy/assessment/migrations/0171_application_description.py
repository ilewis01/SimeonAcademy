# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0170_roommate_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='description',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
