# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0175_auto_20161228_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='document',
            field=models.FileField(default=None, upload_to=b'documents/'),
            preserve_default=True,
        ),
    ]
