# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0119_auto_20160715_0541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='angermanagement',
            old_name='AMComplete',
            new_name='isComplete',
        ),
        migrations.RenameField(
            model_name='asi',
            old_name='AIS_Complete',
            new_name='isComplete',
        ),
        migrations.RenameField(
            model_name='mentalhealth',
            old_name='MHComplete',
            new_name='isComplete',
        ),
        migrations.RenameField(
            model_name='sap',
            old_name='SapComplete',
            new_name='isComplete',
        ),
    ]
