# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0189_auto_20170126_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ais_drug1',
            name='d13',
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d13Day',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais_drug1',
            name='d13Year',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
