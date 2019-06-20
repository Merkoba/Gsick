# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0017_auto_20160302_0450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='info1',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='info2',
        ),
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 660092)),
        ),
        migrations.AlterField(
            model_name='ban',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 663668)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 655858)),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 664420)),
        ),
        migrations.AlterField(
            model_name='follow',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 661263)),
        ),
        migrations.AlterField(
            model_name='paste',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 662995)),
        ),
        migrations.AlterField(
            model_name='pin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 656853)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 654687)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_bumped',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 654762)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 654740)),
        ),
        migrations.AlterField(
            model_name='privatemessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 657665)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 666151)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_entrance',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 666184)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 665231)),
        ),
        migrations.AlterField(
            model_name='visited',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 59, 12, 662104)),
        ),
    ]
