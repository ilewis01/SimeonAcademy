# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0161_application_work_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='isAuthorized',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
