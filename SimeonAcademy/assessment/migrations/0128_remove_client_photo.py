# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0127_client_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='photo',
        ),
    ]
