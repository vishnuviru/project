# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Tollapp', '0006_auto_20170411_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='Location',
            field=models.CharField(default=b'TADA', max_length=100),
        ),
        migrations.AlterField(
            model_name='anpr',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 506082)),
        ),
        migrations.AlterField(
            model_name='axle_count',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 510370)),
        ),
        migrations.AlterField(
            model_name='log_details',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 507184)),
        ),
        migrations.AlterField(
            model_name='login_details',
            name='L1_Login',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 512299)),
        ),
        migrations.AlterField(
            model_name='main',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 503522)),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 511078)),
        ),
        migrations.AlterField(
            model_name='officer',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 506633)),
        ),
        migrations.AlterField(
            model_name='ping',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 511756)),
        ),
        migrations.AlterField(
            model_name='sensor_details',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 507865)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Created_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 504644)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Updated_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 504666)),
        ),
        migrations.AlterField(
            model_name='weigh_bridge',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 14, 53, 26, 509930)),
        ),
    ]
