# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0008_auto_20160318_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('drug', models.CharField(default=None, max_length=35, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
