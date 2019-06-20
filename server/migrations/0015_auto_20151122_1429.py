# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0014_auto_20151111_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='ban',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 498107)),
        ),
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 489788)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 481515)),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 498977)),
        ),
        migrations.AlterField(
            model_name='follow',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 491299)),
        ),
        migrations.AlterField(
            model_name='paste',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 497319)),
        ),
        migrations.AlterField(
            model_name='pin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 482485)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 480402)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 480442)),
        ),
        migrations.AlterField(
            model_name='privatemessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 483342)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 505067)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_entrance',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 505113)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 499883)),
        ),
        migrations.AlterField(
            model_name='visited',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 14, 29, 49, 496335)),
        ),
    ]
