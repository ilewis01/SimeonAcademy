# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0163_auto_20161116_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoommateEvaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hasCheckstubs', models.BooleanField(default=False)),
                ('hasId', models.BooleanField(default=False)),
                ('ref1_verified', models.BooleanField(default=False)),
                ('ref2_verified', models.BooleanField(default=False)),
                ('ref3_verified', models.BooleanField(default=False)),
                ('work_verified', models.BooleanField(default=False)),
                ('isCandidate', models.BooleanField(default=False)),
                ('application', models.ForeignKey(default=None, blank=True, to='assessment.Application', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
