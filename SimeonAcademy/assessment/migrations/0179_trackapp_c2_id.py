# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0178_attachment_iscouple'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackapp',
            name='c2_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
