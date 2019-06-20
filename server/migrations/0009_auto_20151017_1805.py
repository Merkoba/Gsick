# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_auto_20151017_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='enabled',
        ),
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 18, 5, 4, 763610)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 18, 5, 4, 758419)),
        ),
        migrations.AlterField(
            model_name='follow',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 18, 5, 4, 764743)),
        ),
        migrations.AlterField(
            model_name='paste',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 18, 5, 4, 766482)),
        ),
        migrations.AlterField(
            model_name='pin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 18, 5, 4, 759355)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 18, 5, 4, 757459)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 18, 5, 4, 757496)),
        ),
        migrations.AlterField(
            model_name='privatemessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 18, 5, 4, 760249)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 18, 5, 4, 768666)),
        ),
        migrations.AlterField(
            model_name='visited',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 18, 5, 4, 765666)),
        ),
    ]
