# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0185_treatmentresource_ishandicap'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crafft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_assessment', models.DateField(default=None, null=True, blank=True)),
                ('a1', models.BooleanField(default=False)),
                ('a2', models.BooleanField(default=False)),
                ('a3', models.BooleanField(default=False)),
                ('b1', models.BooleanField(default=False)),
                ('b2', models.BooleanField(default=False)),
                ('b3', models.BooleanField(default=False)),
                ('b4', models.BooleanField(default=False)),
                ('b5', models.BooleanField(default=False)),
                ('b6', models.BooleanField(default=False)),
                ('isOpen', models.BooleanField(default=False)),
                ('isComplete', models.BooleanField(default=False)),
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
