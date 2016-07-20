# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0125_trackapp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='G_Form_ID',
        ),
        migrations.DeleteModel(
            name='G_Session_ID',
        ),
        migrations.AddField(
            model_name='trackapp',
            name='f_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trackapp',
            name='s_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trackapp',
            name='state',
            field=models.ForeignKey(default=None, blank=True, to='assessment.SolidState', null=True),
            preserve_default=True,
        ),
    ]
