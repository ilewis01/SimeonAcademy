# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0145_client_ispending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='isPending',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
