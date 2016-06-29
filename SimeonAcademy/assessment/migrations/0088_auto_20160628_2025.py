# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0087_auto_20160628_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mhdemographic',
            name='bothers',
            field=models.CharField(default=None, max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhdemographic',
            name='childrenFemale',
            field=models.CharField(default=None, max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhdemographic',
            name='childrenMale',
            field=models.CharField(default=None, max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mhdemographic',
            name='sisters',
            field=models.CharField(default=None, max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
