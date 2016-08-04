# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0143_auto_20160729_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='probation_phone',
            field=models.CharField(default=None, max_length=14, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='work_phone',
            field=models.CharField(default=None, max_length=14, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(default=b'/static/images/defaultAvatar.jpg', null=True, upload_to=b'./profile/', blank=True),
            preserve_default=True,
        ),
    ]
