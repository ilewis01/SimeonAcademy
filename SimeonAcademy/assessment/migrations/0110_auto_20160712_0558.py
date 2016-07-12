# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0109_auto_20160711_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ais_legal',
            name='l1',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_legal',
            name='l2',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_legal',
            name='l24',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_legal',
            name='l31',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ais_legal',
            name='l32',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
