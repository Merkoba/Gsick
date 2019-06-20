# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0016_auto_20160227_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privatemessage',
            old_name='info1',
            new_name='info',
        ),
        migrations.RemoveField(
            model_name='privatemessage',
            name='info2',
        ),
        migrations.AddField(
            model_name='post',
            name='info',
            field=models.CharField(default=b'', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 824266)),
        ),
        migrations.AlterField(
            model_name='ban',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 828179)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 819571)),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 828944)),
        ),
        migrations.AlterField(
            model_name='follow',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 825590)),
        ),
        migrations.AlterField(
            model_name='paste',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 827361)),
        ),
        migrations.AlterField(
            model_name='pin',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 820631)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 818380)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_bumped',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 818443)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 818420)),
        ),
        migrations.AlterField(
            model_name='privatemessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 821509)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 830970)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_entrance',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 831014)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 829872)),
        ),
        migrations.AlterField(
            model_name='visited',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 4, 50, 47, 826503)),
        ),
    ]
