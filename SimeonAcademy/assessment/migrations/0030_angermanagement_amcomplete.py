# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0029_auto_20160321_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='angermanagement',
            name='AMComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
