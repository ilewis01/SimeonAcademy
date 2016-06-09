# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0056_am_demographic_whatmedicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='am_angerhistory',
            name='recentVDate',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
