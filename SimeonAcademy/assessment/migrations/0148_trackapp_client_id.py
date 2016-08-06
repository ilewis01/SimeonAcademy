# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0147_auto_20160805_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackapp',
            name='client_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
