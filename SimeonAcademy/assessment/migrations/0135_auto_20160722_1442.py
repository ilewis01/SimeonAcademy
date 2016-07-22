# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0134_auto_20160722_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(default=b'/media/profile/NoImageAvailableMale.jpg', null=True, upload_to=b'/media/profile/', blank=True),
            preserve_default=True,
        ),
    ]
