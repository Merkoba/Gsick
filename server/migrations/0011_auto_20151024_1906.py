# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_auto_20151020_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ban',
            name='user',
        ),
        migrations.AddField(
            model_name='ban',
            name='username',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 19, 6, 29, 173462)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 19, 6, 29, 168549)),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 19, 6, 29, 178190)),
        ),
        migrations.AlterField(
            model_name='follow',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 19, 6, 29, 174516)),
        ),
        migrations.AlterField(
            model_name='paste',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 19, 6, 29, 176241)),
        ),
        migrations.AlterField(
            model_name='pin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 19, 6, 29, 169460)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 19, 6, 29, 167563)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 19, 6, 29, 167597)),
        ),
        migrations.AlterField(
            model_name='privatemessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 19, 6, 29, 170276)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 19, 6, 29, 179159)),
        ),
        migrations.AlterField(
            model_name='visited',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 19, 6, 29, 175437)),
        ),
    ]
