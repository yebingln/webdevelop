# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-14 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20180113_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTpye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]