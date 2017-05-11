# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Tollapp', '0007_auto_20170412_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Lane_Number', models.CharField(default=b'NA', max_length=200)),
                ('Direction', models.CharField(default=b'NA', max_length=200)),
                ('Location', models.CharField(default=b'NA', max_length=200)),
                ('Vehicle_Class', models.CharField(default=b'NA', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='anpr',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 664353)),
        ),
        migrations.AlterField(
            model_name='axle_count',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 668681)),
        ),
        migrations.AlterField(
            model_name='log_details',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 665530)),
        ),
        migrations.AlterField(
            model_name='login_details',
            name='L1_Login',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 670592)),
        ),
        migrations.AlterField(
            model_name='main',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 661909)),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 669386)),
        ),
        migrations.AlterField(
            model_name='officer',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 664885)),
        ),
        migrations.AlterField(
            model_name='ping',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 670054)),
        ),
        migrations.AlterField(
            model_name='sensor_details',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 666213)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Created_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 663028)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Updated_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 663051)),
        ),
        migrations.AlterField(
            model_name='weigh_bridge',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 18, 11, 33, 27, 668246)),
        ),
    ]
