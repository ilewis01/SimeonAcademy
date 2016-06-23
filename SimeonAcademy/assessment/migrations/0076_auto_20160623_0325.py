# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0075_auto_20160621_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='sap',
            name='clinicPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='otherPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='psycho1Priority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='psycho2Priority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='socialPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='sourcesPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='spacialPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
