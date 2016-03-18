# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0003_dependents_livingsituation_residence'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dependents',
        ),
        migrations.DeleteModel(
            name='Residence',
        ),
    ]
