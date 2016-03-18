# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0018_auto_20160318_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentalHealth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
