# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import awesome_avatar.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0129_client_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=awesome_avatar.fields.AvatarField(default=None, null=True, upload_to=b'avatars', blank=True),
            preserve_default=True,
        ),
    ]
