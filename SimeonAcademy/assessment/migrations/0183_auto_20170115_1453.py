# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0182_attachment_clientid2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='date',
            field=models.DateField(default=None, auto_now_add=True),
            preserve_default=True,
        ),
    ]
