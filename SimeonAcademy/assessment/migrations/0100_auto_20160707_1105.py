# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0099_auto_20160707_1055'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EducationLevel',
        ),
        migrations.DeleteModel(
            name='LivingSituation',
        ),
        migrations.DeleteModel(
            name='MaritalStatus',
        ),
    ]
