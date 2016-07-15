# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0116_auto_20160714_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsession',
            name='noServices',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
