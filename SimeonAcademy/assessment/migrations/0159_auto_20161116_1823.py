# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0158_auto_20161116_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('lastName', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('phone', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('ssn', models.CharField(default=None, max_length=11, null=True, blank=True)),
                ('occupation', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('photo', models.ImageField(default=b'/static/images/defaultAvatar.jpg', null=True, upload_to=b'./profile/', blank=True)),
                ('isMale', models.BooleanField(default=False)),
                ('hasCheckstubs', models.BooleanField(default=False)),
                ('hasId', models.BooleanField(default=False)),
                ('ref1', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('ref1_phone', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('ref1_verified', models.BooleanField(default=False)),
                ('ref2', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('ref2_phone', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('ref2_verified', models.BooleanField(default=False)),
                ('ref3', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('ref3_phone', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('ref3_verified', models.BooleanField(default=False)),
                ('isCandidate', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='hasCheckstubs',
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='hasId',
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='ref1',
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='ref1_phone',
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='ref1_verified',
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='ref2',
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='ref2_phone',
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='ref2_verified',
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='ref3',
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='ref3_phone',
        ),
        migrations.RemoveField(
            model_name='roommate',
            name='ref3_verified',
        ),
    ]
