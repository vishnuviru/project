# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Tollapp', '0011_auto_20170428_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_Time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User_Name', models.CharField(default=b'NA', max_length=200)),
                ('Lane_Number', models.CharField(default=b'NA', max_length=200)),
                ('Direction', models.CharField(default=b'NA', max_length=200)),
                ('Login_Time', models.CharField(default=b'NA', max_length=200)),
                ('Logout_Time', models.CharField(default=b'NA', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Login_Details',
        ),
        migrations.AlterField(
            model_name='anpr',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 53, 22, 945320)),
        ),
        migrations.AlterField(
            model_name='axle_count',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 53, 22, 949492)),
        ),
        migrations.AlterField(
            model_name='log_details',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 53, 22, 946379)),
        ),
        migrations.AlterField(
            model_name='main',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 53, 22, 942832)),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 53, 22, 950170)),
        ),
        migrations.AlterField(
            model_name='officer',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 53, 22, 945844)),
        ),
        migrations.AlterField(
            model_name='ping',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 53, 22, 950825)),
        ),
        migrations.AlterField(
            model_name='sensor_details',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 53, 22, 947039)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Created_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 53, 22, 943909)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Updated_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 53, 22, 943929)),
        ),
        migrations.AlterField(
            model_name='weigh_bridge',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 3, 16, 53, 22, 949062)),
        ),
    ]
