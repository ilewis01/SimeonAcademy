# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0113_auto_20160712_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashPay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('received', models.IntegerField(default=0)),
                ('oweChange', models.BooleanField(default=False)),
                ('changeAmt', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CheckPay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('accountNumber', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('routingNumber', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('checkNumber', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('address', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('city', models.CharField(default=None, max_length=20, null=True, blank=True)),
                ('zipCode', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('received', models.IntegerField(default=0)),
                ('state', models.ForeignKey(default=None, blank=True, to='assessment.State', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreditPay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameOnCard', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('cardNumber', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('expDate', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('CRV', models.CharField(default=None, max_length=7, null=True, blank=True)),
                ('zipCode', models.CharField(default=None, max_length=10, null=True, blank=True)),
                ('isApproved', models.BooleanField(default=False)),
                ('received', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InsurancePay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('InsuranceCompany', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('accountNumber', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('accountName', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('received', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paymentType', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('date', models.DateField(default=None, null=True, blank=True)),
                ('isPartial', models.BooleanField(default=False)),
                ('received', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='amount',
            new_name='grandTotal',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='billed_to',
        ),
        migrations.AddField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(default=None, blank=True, to='assessment.Client', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='isPaid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='partialPaid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='quantity1',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='quantity2',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='quantity3',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='quantity4',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='quantity5',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='quantity6',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='total1',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='total2',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='total3',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='total4',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='total5',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='total6',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='urineresults',
            name='isPaid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug1',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug10',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug11',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug2',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug3',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug4',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug5',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug6',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug7',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug8',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='urineresults',
            name='drug9',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
