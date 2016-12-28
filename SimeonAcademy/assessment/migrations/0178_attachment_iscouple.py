# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0177_auto_20161228_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='isCouple',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
