# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0174_application_israted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('date', models.DateField(default=None, null=True, blank=True)),
                ('title', models.CharField(default=None, max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Couple',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id1', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('id2', models.CharField(default=None, max_length=30, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='note',
            name='isCouple',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
