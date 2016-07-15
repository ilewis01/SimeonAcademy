# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0117_auto_20160715_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discharge',
            name='isOpen',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
