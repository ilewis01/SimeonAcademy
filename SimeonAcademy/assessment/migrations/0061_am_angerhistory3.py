# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0060_auto_20160609_0519'),
    ]

    operations = [
        migrations.CreateModel(
            name='AM_AngerHistory3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_id', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('date_of_assessment', models.DateField(default=None, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
