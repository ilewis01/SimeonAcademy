# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import awesome_avatar.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0130_auto_20160722_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=awesome_avatar.fields.AvatarField(default=None, null=True, upload_to=b'media/profile/', blank=True),
            preserve_default=True,
        ),
    ]
