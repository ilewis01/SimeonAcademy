# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0132_auto_20160722_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to=b'/static/media/profile/', blank=True),
            preserve_default=True,
        ),
    ]
