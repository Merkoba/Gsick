# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_auto_20151024_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='info3',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='user3',
        ),
        migrations.AddField(
            model_name='alert',
            name='comment1',
            field=models.ForeignKey(related_name='comment_1', to='server.Comment', null=True),
        ),
        migrations.AddField(
            model_name='alert',
            name='comment2',
            field=models.ForeignKey(related_name='comment_2', to='server.Comment', null=True),
        ),
        migrations.AddField(
            model_name='alert',
            name='post1',
            field=models.ForeignKey(related_name='post_1', to='server.Post', null=True),
        ),
        migrations.AddField(
            model_name='alert',
            name='post2',
            field=models.ForeignKey(related_name='post_2', to='server.Post', null=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 15, 52, 863137)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 15, 52, 858057)),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 15, 52, 868113)),
        ),
        migrations.AlterField(
            model_name='follow',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 15, 52, 864452)),
        ),
        migrations.AlterField(
            model_name='paste',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 15, 52, 866095)),
        ),
        migrations.AlterField(
            model_name='pin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 15, 52, 859011)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 15, 52, 857025)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 15, 52, 857066)),
        ),
        migrations.AlterField(
            model_name='privatemessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 15, 52, 859823)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 15, 52, 869060)),
        ),
        migrations.AlterField(
            model_name='visited',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 25, 21, 15, 52, 865325)),
        ),
    ]
