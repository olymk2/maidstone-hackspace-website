# Generated by Django 2.1.1 on 2019-01-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_increased_rfid_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='has_fob',
            field=models.BooleanField(default=False, help_text='Member has fob access'),
        ),
    ]
