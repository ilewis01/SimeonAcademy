# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0122_clientsession_hasinvoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='G_Form_ID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('g_id', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Global_Session_ID',
            new_name='G_Session_ID',
        ),
        migrations.DeleteModel(
            name='global_ID',
        ),
        migrations.RenameField(
            model_name='g_session_id',
            old_name='global_id',
            new_name='s_id',
        ),
    ]
