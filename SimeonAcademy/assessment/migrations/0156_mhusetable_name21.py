# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0155_auto_20160929_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='mhusetable',
            name='name21',
            field=models.CharField(default=None, max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
    ]
