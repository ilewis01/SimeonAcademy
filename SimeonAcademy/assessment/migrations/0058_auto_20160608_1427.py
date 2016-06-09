# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0057_auto_20160608_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='am_angerhistory',
            name='howfeelRecentV',
        ),
        migrations.AddField(
            model_name='am_angerhistory',
            name='feltStrong',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory',
            name='hadRush',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_angerhistory',
            name='wasTense',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
