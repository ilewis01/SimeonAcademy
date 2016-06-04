# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0050_auto_20160408_0643'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsession',
            name='isComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
