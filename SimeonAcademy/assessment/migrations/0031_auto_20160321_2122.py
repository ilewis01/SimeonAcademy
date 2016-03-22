# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0030_angermanagement_amcomplete'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentalhealth',
            name='MHComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='activitiesComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='demographicsComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='educationComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='familyComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='familyHistoryComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='legalHistoryComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='relationshipsComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='stressorsComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='useTableComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
