# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.CharField(max_length=250),
        ),
    ]
