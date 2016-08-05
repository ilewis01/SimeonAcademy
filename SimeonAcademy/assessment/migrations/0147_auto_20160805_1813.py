# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0146_auto_20160804_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='hasFiles',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='isRemoved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
