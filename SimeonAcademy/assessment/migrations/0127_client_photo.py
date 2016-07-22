# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0126_auto_20160720_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(upload_to=b'/images/profile', blank=True),
            preserve_default=True,
        ),
    ]
