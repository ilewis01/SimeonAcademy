# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0153_remove_am_worstepisode_threatsworst'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('date', models.DateField(default=None, null=True, blank=True)),
                ('title', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('note', models.CharField(default=None, max_length=5000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
