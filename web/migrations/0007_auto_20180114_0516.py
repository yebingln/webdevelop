# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-14 05:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_userinfo_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserTpye'),
        ),
    ]
