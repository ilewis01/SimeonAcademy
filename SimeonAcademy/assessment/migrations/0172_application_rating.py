# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0171_application_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
