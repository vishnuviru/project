# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Tollapp', '0012_auto_20170503_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anpr',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 820214)),
        ),
        migrations.AlterField(
            model_name='axle_count',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 824452)),
        ),
        migrations.AlterField(
            model_name='log_details',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 821309)),
        ),
        migrations.AlterField(
            model_name='login_time',
            name='Login_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 826457)),
        ),
        migrations.AlterField(
            model_name='login_time',
            name='Logout_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 826477)),
        ),
        migrations.AlterField(
            model_name='main',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 817741)),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 825225)),
        ),
        migrations.AlterField(
            model_name='officer',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 820746)),
        ),
        migrations.AlterField(
            model_name='ping',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 825903)),
        ),
        migrations.AlterField(
            model_name='sensor_details',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 821990)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Created_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 818866)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Updated_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 818888)),
        ),
        migrations.AlterField(
            model_name='weigh_bridge',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 57, 36, 824016)),
        ),
    ]
