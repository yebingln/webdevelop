# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-13 09:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20180113_0527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ass',
            old_name='creat_date',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='ass',
            old_name='update_data',
            new_name='update_date',
        ),
    ]
