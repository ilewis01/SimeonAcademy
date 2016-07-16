# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0121_global_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsession',
            name='hasInvoice',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
