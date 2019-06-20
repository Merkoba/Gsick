# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('server', '0003_auto_20151005_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='user2',
            field=models.ForeignKey(related_name='alert_user_2', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='alert',
            name='user3',
            field=models.ForeignKey(related_name='alert_user_3', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 1, 33, 14, 55428)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 1, 33, 14, 49502)),
        ),
        migrations.AlterField(
            model_name='follow',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 1, 33, 14, 56533)),
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 1, 33, 14, 51272)),
        ),
        migrations.AlterField(
            model_name='paste',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 1, 33, 14, 58101)),
        ),
        migrations.AlterField(
            model_name='pin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 1, 33, 14, 50437)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 1, 33, 14, 48470)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 1, 33, 14, 48511)),
        ),
        migrations.AlterField(
            model_name='privatemessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 9, 1, 33, 14, 52092)),
        ),
    ]
