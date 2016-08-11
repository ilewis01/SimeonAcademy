# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0148_trackapp_client_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('counselor_id', models.IntegerField(default=0)),
                ('counselor', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('date', models.DateField(default=None, null=True, blank=True)),
                ('startHr', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('startMin', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('endHr', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('endMin', models.CharField(default=None, max_length=2, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='appointment',
            name='counselor',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='counselor_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
