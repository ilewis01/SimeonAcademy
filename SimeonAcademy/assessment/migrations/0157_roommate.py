# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0156_mhusetable_name21'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roommate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('phone', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('occupation', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('viewDate', models.DateField(default=None, null=True, blank=True)),
                ('isMale', models.BooleanField(default=False)),
                ('notes', models.CharField(default=None, max_length=400, null=True, blank=True)),
                ('photo', models.ImageField(default=b'/static/images/defaultAvatar.jpg', null=True, upload_to=b'./profile/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
