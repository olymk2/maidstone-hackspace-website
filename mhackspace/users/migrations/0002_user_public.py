# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='public',
            field=models.BooleanField(default=False, help_text='If the users email is public on post feeds'),
        ),
    ]
