# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0037_auto_20160404_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='angermanagement',
            name='angerHistory',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_AngerHistory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='angerHistoryComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='angerTarget',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_AngerTarget', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='angerTargetComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='childhood',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_ChildhoodHistory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='childhoodComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='connections',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_Connections', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='connectionsComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='control',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_Control', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='controlComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='currentProblems',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_CurrentProblem', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='currentProblemsComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='demographic',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_Demographic', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='demographicComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='drugHistory',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_DrugHistory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='drugHistoryComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='familyOrigin',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_FamilyOrigin', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='familyOriginComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='final',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_Final', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='finalComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='worstComplete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='angermanagement',
            name='worstEpisode',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AM_WorstEpisode', null=True),
            preserve_default=True,
        ),
    ]
