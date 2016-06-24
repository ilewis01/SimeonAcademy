# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0078_auto_20160624_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentalhealth',
            name='client',
            field=models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True),
            preserve_default=True,
        ),
    ]
