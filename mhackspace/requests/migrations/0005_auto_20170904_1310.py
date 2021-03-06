# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 13:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0004_auto_20170904_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequests',
            name='cost',
            field=models.DecimalField(decimal_places=2, help_text='Leave blank, if no associated cost, or add estimated cost if not sure.', max_digits=4),
        ),
        migrations.AlterField(
            model_name='userrequests',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
