# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0179_trackapp_c2_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(default=b'profile/defaultAvatar.jpg', null=True, upload_to=b'./profile/', blank=True),
            preserve_default=True,
        ),
    ]
