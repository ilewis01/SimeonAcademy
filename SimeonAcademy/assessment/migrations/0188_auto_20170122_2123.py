# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0187_crafft_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crafft',
            old_name='isComplete',
            new_name='positiveScreen',
        ),
        migrations.RemoveField(
            model_name='crafft',
            name='isOpen',
        ),
    ]
