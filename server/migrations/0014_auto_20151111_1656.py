# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0013_auto_20151111_0047'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.RemoveField(
            model_name='silenced',
            name='brat',
        ),
        migrations.RemoveField(
            model_name='silenced',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='num_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='num_comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='num_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 599642)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 595081)),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 604152)),
        ),
        migrations.AlterField(
            model_name='follow',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 601016)),
        ),
        migrations.AlterField(
            model_name='paste',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 602754)),
        ),
        migrations.AlterField(
            model_name='pin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 596146)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 593947)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 593984)),
        ),
        migrations.AlterField(
            model_name='privatemessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 597029)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 605982)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_entrance',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 606017)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 605021)),
        ),
        migrations.AlterField(
            model_name='visited',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 11, 16, 56, 17, 601949)),
        ),
        migrations.DeleteModel(
            name='Silenced',
        ),
    ]
