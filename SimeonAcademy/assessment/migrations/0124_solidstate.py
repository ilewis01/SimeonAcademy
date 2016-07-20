# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0123_auto_20160720_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolidState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('url', models.CharField(default=None, max_length=25, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
