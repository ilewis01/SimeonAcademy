# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0077_sap_isopen'),
    ]

    operations = [
        migrations.AddField(
            model_name='angermanagement',
            name='isOpen',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='isOpen',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='urineresults',
            name='isComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='urineresults',
            name='isOpen',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
