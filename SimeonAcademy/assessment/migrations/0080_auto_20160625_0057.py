# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0079_mentalhealth_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='angermanagement',
            name='ah1Priority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='ah2Priority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='ah3Priority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='childPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='connectPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='controlPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='currentPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='date_of_assessment',
            field=models.DateField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='demoPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='dhPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='familyPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='finalPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='targetPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='worstPriority',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
