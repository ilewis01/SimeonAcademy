# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0166_auto_20161116_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommateevaluation',
            name='personality',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
