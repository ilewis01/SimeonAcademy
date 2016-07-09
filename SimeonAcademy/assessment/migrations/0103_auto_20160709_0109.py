# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0102_auto_20160707_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urineresults',
            old_name='testDate',
            new_name='date_of_assessment',
        ),
        migrations.RemoveField(
            model_name='urineresults',
            name='drug12',
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug1',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug10',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug11',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug2',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug3',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug4',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug5',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug6',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug7',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug8',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug9',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
