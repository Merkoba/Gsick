# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0015_auto_20151122_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_bumped',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 634997)),
        ),
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 645359)),
        ),
        migrations.AlterField(
            model_name='ban',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 651652)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 637255)),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 652944)),
        ),
        migrations.AlterField(
            model_name='follow',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 647548)),
        ),
        migrations.AlterField(
            model_name='paste',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 650429)),
        ),
        migrations.AlterField(
            model_name='pin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 639268)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 634861)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 634939)),
        ),
        migrations.AlterField(
            model_name='privatemessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 640770)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 656004)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_entrance',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 656067)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 654350)),
        ),
        migrations.AlterField(
            model_name='visited',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 21, 14, 54, 649072)),
        ),
    ]
