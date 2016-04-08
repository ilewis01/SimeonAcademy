# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0049_auto_20160406_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='am_drughistory',
            name='isClean',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
