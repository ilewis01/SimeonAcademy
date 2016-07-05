# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0095_auto_20160702_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='AIS',
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AIS_Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('g1', models.CharField(default=None, max_length=4, null=True, blank=True)),
                ('g2', models.CharField(default=None, max_length=4, null=True, blank=True)),
                ('g3', models.CharField(default=None, max_length=4, null=True, blank=True)),
                ('g4', models.DateField(default=None, null=True, blank=True)),
                ('g8', models.IntegerField(default=0)),
                ('g9', models.IntegerField(default=0)),
                ('g10', models.IntegerField(default=0)),
                ('g11', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('g12', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AIS_Drug1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('d1Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d1Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d1Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d2Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d2Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d2Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d3Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d3Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d3Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d4Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d4Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d4Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d5Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d5Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d5Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d6Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d6Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d6Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d7Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d7Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d7Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d8Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d8Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d8Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d9Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d9Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d9Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d10Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d10Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d10Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d11Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d11Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d11Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d12Day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d12Year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d12Route', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d13', models.CharField(default=None, max_length=1, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AIS_Drug2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('d14', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d15', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d16', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d17', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d18', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d19', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d20', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d21', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d22', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d23', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d24', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d25', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d26', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d27', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d28', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d29', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('d30', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d31', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d32', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d33', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('d34', models.BooleanField(default=False)),
                ('d35', models.BooleanField(default=False)),
                ('comments', models.CharField(default=None, max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AIS_Employment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('e1yrs', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('e1mth', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('e2', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('e3', models.BooleanField(default=False)),
                ('e3Exp', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('e4', models.BooleanField(default=False)),
                ('e5', models.BooleanField(default=False)),
                ('e5Exp', models.BooleanField(default=False)),
                ('e6yrs', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('e6mth', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('e7', models.BooleanField(default=False)),
                ('e7Exp', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('e8', models.BooleanField(default=False)),
                ('e9', models.BooleanField(default=False)),
                ('e10', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('e11', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('e12', models.CharField(default=None, max_length=4, null=True, blank=True)),
                ('e13', models.CharField(default=None, max_length=4, null=True, blank=True)),
                ('e14', models.CharField(default=None, max_length=4, null=True, blank=True)),
                ('e15', models.CharField(default=None, max_length=4, null=True, blank=True)),
                ('e16', models.CharField(default=None, max_length=4, null=True, blank=True)),
                ('e17', models.CharField(default=None, max_length=4, null=True, blank=True)),
                ('e18', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('e19', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('e20', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('e21', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('e22', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('e23', models.BooleanField(default=False)),
                ('e24', models.BooleanField(default=False)),
                ('comments', models.CharField(default=None, max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AIS_Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('h1a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h1d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h1p', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h2a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h2d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h2p', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h3a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h3d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h3p', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h4a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h4d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h4p', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h5a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h5d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h5p', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h6a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h6d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h6p', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h7a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h7d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h7p', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h8a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h8d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h8p', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h9a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h9d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h9p', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h10a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h10d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h10p', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h11a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h11d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h11p', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h12a', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h12d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('h12p', models.CharField(default=None, max_length=1, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AIS_General',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('g13', models.CharField(default=None, max_length=3, null=True, blank=True)),
                ('g14yrs', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('g14mos', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('g15', models.BooleanField(default=False)),
                ('g16mth', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('g16day', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('g16year', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('g17', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('g18', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('g19', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('g20', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('g21', models.CharField(default=None, max_length=3, null=True, blank=True)),
                ('g22', models.CharField(default=None, max_length=3, null=True, blank=True)),
                ('g23', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('g24', models.CharField(default=None, max_length=3, null=True, blank=True)),
                ('g25', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('g26', models.CharField(default=None, max_length=3, null=True, blank=True)),
                ('g27', models.CharField(default=None, max_length=3, null=True, blank=True)),
                ('g28', models.CharField(default=None, max_length=3, null=True, blank=True)),
                ('medical', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('employ', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('alcohol', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('drug', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('legal', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('family', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('psych', models.CharField(default=None, max_length=1, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AIS_Legal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('l1', models.BooleanField(default=False)),
                ('l2', models.BooleanField(default=False)),
                ('l3', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l4', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l5', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l6', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l7', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l8', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l9', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l10', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l11', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l12', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l13', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l14', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l15', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l16', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l17', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l18', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l19', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l20', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l21', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l22', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l23', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l24', models.BooleanField(default=False)),
                ('l25', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l26', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l27', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('l28', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('l29', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('l30', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('l31', models.BooleanField(default=False)),
                ('l32', models.BooleanField(default=False)),
                ('comments', models.CharField(default=None, max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AIS_Medical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('m1', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('m2yrs', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('m2mth', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('m3', models.BooleanField(default=False)),
                ('m4', models.BooleanField(default=False)),
                ('m5', models.BooleanField(default=False)),
                ('m5Exp', models.CharField(default=None, max_length=100, null=True, blank=True)),
                ('m6', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('m7', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('m8', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('m9', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('m10', models.BooleanField(default=False)),
                ('m11', models.BooleanField(default=False)),
                ('comments', models.CharField(default=None, max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AIS_Psych',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('p1', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('p2', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('p3', models.BooleanField(default=False)),
                ('p4d', models.BooleanField(default=False)),
                ('p4y', models.BooleanField(default=False)),
                ('p5d', models.BooleanField(default=False)),
                ('p5y', models.BooleanField(default=False)),
                ('p6d', models.BooleanField(default=False)),
                ('p6y', models.BooleanField(default=False)),
                ('p7d', models.BooleanField(default=False)),
                ('p7y', models.BooleanField(default=False)),
                ('p8d', models.BooleanField(default=False)),
                ('p8y', models.BooleanField(default=False)),
                ('p9d', models.BooleanField(default=False)),
                ('p9y', models.BooleanField(default=False)),
                ('p10d', models.BooleanField(default=False)),
                ('p10y', models.BooleanField(default=False)),
                ('p11d', models.BooleanField(default=False)),
                ('p11y', models.BooleanField(default=False)),
                ('p12', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('p13', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('p14', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('p15', models.BooleanField(default=False)),
                ('p16', models.BooleanField(default=False)),
                ('p17', models.BooleanField(default=False)),
                ('p18', models.BooleanField(default=False)),
                ('p19', models.BooleanField(default=False)),
                ('p20', models.BooleanField(default=False)),
                ('p21', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('p22', models.BooleanField(default=False)),
                ('p23', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AIS_Social1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('f1', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f2yrs', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('f2mth', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('f3', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f4', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f5yrs', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('f5mth', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('f6', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f7', models.BooleanField(default=False)),
                ('f8', models.BooleanField(default=False)),
                ('f9', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f10', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f11', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f30', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('f31', models.CharField(default=None, max_length=2, null=True, blank=True)),
                ('f32', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f33', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f34', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f35', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f36', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f37', models.BooleanField(default=False)),
                ('f38', models.BooleanField(default=False)),
                ('comments', models.CharField(default=None, max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AIS_Social2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientID', models.CharField(default=None, max_length=30, null=True, blank=True)),
                ('f12', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f13', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f14', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f16', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f17', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f18d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f18y', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f19d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f19y', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f20d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f20y', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f21d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f21y', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f22d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f22y', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f23d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f23y', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f24d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f24y', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f25d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f25y', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f26d', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f26y', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('fa18', models.BooleanField(default=False)),
                ('fa19', models.BooleanField(default=False)),
                ('fa20', models.BooleanField(default=False)),
                ('fa21', models.BooleanField(default=False)),
                ('fa22', models.BooleanField(default=False)),
                ('fa23', models.BooleanField(default=False)),
                ('fa24', models.BooleanField(default=False)),
                ('fa25', models.BooleanField(default=False)),
                ('fa26', models.BooleanField(default=False)),
                ('f18dayBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f18yearBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f19dayBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f19yearBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f20dayBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f20yearBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f21dayBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f21yearBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f22dayBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f22yearBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f23dayBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f23yearBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f24dayBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f24yearBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f25dayBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f25yearBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f26dayBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('f26yearBad', models.CharField(default=None, max_length=1, null=True, blank=True)),
                ('comments', models.CharField(default=None, max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ais',
            name='admin',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AIS_Admin', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais',
            name='client',
            field=models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais',
            name='drug1',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AIS_Drug1', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais',
            name='drug2',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AIS_Drug2', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais',
            name='employment',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AIS_Employment', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais',
            name='family',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AIS_Family', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais',
            name='general',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AIS_General', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais',
            name='legal',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AIS_Legal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais',
            name='medical',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AIS_Medical', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais',
            name='psych',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AIS_Psych', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais',
            name='social1',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AIS_Social1', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ais',
            name='social2',
            field=models.ForeignKey(default=None, blank=True, to='assessment.AIS_Social2', null=True),
            preserve_default=True,
        ),
    ]
