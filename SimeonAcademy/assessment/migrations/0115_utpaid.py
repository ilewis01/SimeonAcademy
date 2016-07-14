# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0114_auto_20160713_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='UtPaid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
