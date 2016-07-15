# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0115_utpaid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientsession',
            old_name='end',
            new_name='endTime',
        ),
        migrations.RenameField(
            model_name='clientsession',
            old_name='start',
            new_name='startTime',
        ),
        migrations.RenameField(
            model_name='urineresults',
            old_name='isPaid',
            new_name='initialized',
        ),
        migrations.RemoveField(
            model_name='clientsession',
            name='s_type',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='quantity1',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='quantity2',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='quantity3',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='quantity4',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='quantity5',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='quantity6',
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='initialized',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asi',
            name='initialized',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='counselor',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='isOpen',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='isPaid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientsession',
            name='noServices',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='isOpen',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentalhealth',
            name='initialized',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sap',
            name='initialized',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
