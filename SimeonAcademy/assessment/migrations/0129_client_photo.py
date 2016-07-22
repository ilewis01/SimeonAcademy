# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0128_remove_client_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'static/media/profile/', blank=True),
            preserve_default=True,
        ),
    ]
