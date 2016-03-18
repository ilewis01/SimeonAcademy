# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0012_urineresults'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date1', models.DateField(default=None, null=True, blank=True)),
                ('date2', models.DateField(default=None, null=True, blank=True)),
                ('date3', models.DateField(default=None, null=True, blank=True)),
                ('problem', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('health', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('family', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('psychoactive', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('special', models.CharField(default=None, max_length=500, null=True, blank=True)),
                ('psychological', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('gambling', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('abilities', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('other', models.CharField(default=None, max_length=250, null=True, blank=True)),
                ('source1', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('relationship1', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('source2', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('relationship2', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
