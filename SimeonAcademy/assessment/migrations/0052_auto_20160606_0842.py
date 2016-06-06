# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0051_clientsession_iscomplete'),
    ]

    operations = [
        migrations.AddField(
            model_name='am_familyorigin',
            name='hasLovingMother',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='am_familyorigin',
            name='hasLovingSiblings',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
