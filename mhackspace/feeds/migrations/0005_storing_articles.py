# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 03:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import stdimage.models
import stdimage.utils


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_feed_enabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('original_image', models.URLField(blank=True, max_length=255, null=True)),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to=stdimage.utils.UploadToAutoSlugClassNameDir('title'))),
                ('description', models.TextField()),
                ('displayed', models.BooleanField(default=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='feed',
            name='url',
        ),
        migrations.AddField(
            model_name='feed',
            name='feed_url',
            field=models.URLField(default='http://thearduinoguy.org/?feed=rss2', verbose_name='RSS Feed URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feed',
            name='home_url',
            field=models.URLField(default='http://thearduinoguy.org/', verbose_name='Site Home Page'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feed',
            name='title',
            field=models.CharField(default='The Arduino Guy', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feed',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=stdimage.utils.UploadToAutoSlugClassNameDir('title')),
        ),
        migrations.AddField(
            model_name='article',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.Feed'),
        ),
    ]
