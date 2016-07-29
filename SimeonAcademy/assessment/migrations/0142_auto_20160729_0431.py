# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0141_auto_20160722_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrintableForms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('counselor', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('p1_id', models.IntegerField(default=0)),
                ('p1_type', models.CharField(default=None, max_length=3, null=True, blank=True)),
                ('p2_id', models.IntegerField(default=0)),
                ('p2_type', models.CharField(default=None, max_length=3, null=True, blank=True)),
                ('p3_id', models.IntegerField(default=0)),
                ('p3_type', models.CharField(default=None, max_length=3, null=True, blank=True)),
                ('p4_id', models.IntegerField(default=0)),
                ('p4_type', models.CharField(default=None, max_length=3, null=True, blank=True)),
                ('p5_id', models.IntegerField(default=0)),
                ('p5_type', models.CharField(default=None, max_length=3, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='trackapp',
            name='printable',
            field=models.ForeignKey(default=None, blank=True, to='assessment.PrintableForms', null=True),
            preserve_default=True,
        ),
    ]
