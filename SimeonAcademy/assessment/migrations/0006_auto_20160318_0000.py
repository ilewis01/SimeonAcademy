# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0005_auto_20160317_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(default=None, max_length=35, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='angermanagement',
            name='education',
            field=models.ForeignKey(default=None, blank=True, to='assessment.EducationLevel', null=True),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Education',
        ),
    ]
