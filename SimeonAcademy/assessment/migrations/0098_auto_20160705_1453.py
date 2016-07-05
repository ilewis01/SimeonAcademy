# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0097_ais_psych_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='ASI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_assessment', models.DateField(default=None, null=True, blank=True)),
                ('startTime', models.CharField(default=None, max_length=4, null=True, blank=True)),
                ('endTime', models.CharField(default=None, max_length=4, null=True, blank=True)),
                ('adminComplete', models.BooleanField(default=False)),
                ('generalComplete', models.BooleanField(default=False)),
                ('medicalComplete', models.BooleanField(default=False)),
                ('employmentComplete', models.BooleanField(default=False)),
                ('drug1Complete', models.BooleanField(default=False)),
                ('drug2Complete', models.BooleanField(default=False)),
                ('legalComplete', models.BooleanField(default=False)),
                ('familyComplete', models.BooleanField(default=False)),
                ('social1Complete', models.BooleanField(default=False)),
                ('social2Complete', models.BooleanField(default=False)),
                ('psychComplete', models.BooleanField(default=False)),
                ('adminPriority', models.BooleanField(default=False)),
                ('generalPriority', models.BooleanField(default=False)),
                ('medicalPriority', models.BooleanField(default=False)),
                ('employmentPriority', models.BooleanField(default=False)),
                ('drug1Priority', models.BooleanField(default=False)),
                ('drug2Priority', models.BooleanField(default=False)),
                ('legalPriority', models.BooleanField(default=False)),
                ('familyPriority', models.BooleanField(default=False)),
                ('social1Priority', models.BooleanField(default=False)),
                ('social2Priority', models.BooleanField(default=False)),
                ('psychPriority', models.BooleanField(default=False)),
                ('isOpen', models.BooleanField(default=False)),
                ('AIS_Complete', models.BooleanField(default=False)),
                ('admin', models.ForeignKey(default=None, blank=True, to='assessment.AIS_Admin', null=True)),
                ('client', models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True)),
                ('drug1', models.ForeignKey(default=None, blank=True, to='assessment.AIS_Drug1', null=True)),
                ('drug2', models.ForeignKey(default=None, blank=True, to='assessment.AIS_Drug2', null=True)),
                ('employment', models.ForeignKey(default=None, blank=True, to='assessment.AIS_Employment', null=True)),
                ('family', models.ForeignKey(default=None, blank=True, to='assessment.AIS_Family', null=True)),
                ('general', models.ForeignKey(default=None, blank=True, to='assessment.AIS_General', null=True)),
                ('legal', models.ForeignKey(default=None, blank=True, to='assessment.AIS_Legal', null=True)),
                ('medical', models.ForeignKey(default=None, blank=True, to='assessment.AIS_Medical', null=True)),
                ('psych', models.ForeignKey(default=None, blank=True, to='assessment.AIS_Psych', null=True)),
                ('social1', models.ForeignKey(default=None, blank=True, to='assessment.AIS_Social1', null=True)),
                ('social2', models.ForeignKey(default=None, blank=True, to='assessment.AIS_Social2', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='ais',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='ais',
            name='client',
        ),
        migrations.RemoveField(
            model_name='ais',
            name='drug1',
        ),
        migrations.RemoveField(
            model_name='ais',
            name='drug2',
        ),
        migrations.RemoveField(
            model_name='ais',
            name='employment',
        ),
        migrations.RemoveField(
            model_name='ais',
            name='family',
        ),
        migrations.RemoveField(
            model_name='ais',
            name='general',
        ),
        migrations.RemoveField(
            model_name='ais',
            name='legal',
        ),
        migrations.RemoveField(
            model_name='ais',
            name='medical',
        ),
        migrations.RemoveField(
            model_name='ais',
            name='psych',
        ),
        migrations.RemoveField(
            model_name='ais',
            name='social1',
        ),
        migrations.RemoveField(
            model_name='ais',
            name='social2',
        ),
        migrations.DeleteModel(
            name='AIS',
        ),
    ]
