# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-11 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='Age',
            field=models.IntegerField(default=28),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='CreatData',
            field=models.DateTimeField(default='2018-1-12'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='Gender',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='memo',
            field=models.TextField(default='lalallalala'),
        ),
    ]
