# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0162_application_isauthorized'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='hasCheckstubs',
        ),
        migrations.RemoveField(
            model_name='application',
            name='hasId',
        ),
        migrations.RemoveField(
            model_name='application',
            name='isCandidate',
        ),
    ]
