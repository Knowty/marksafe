# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(unique=True, max_length=20)),
                ('photo', models.ImageField(upload_to=b'refugee_photos', blank=True)),
                ('notification_contact_number', models.CharField(max_length=20, blank=True)),
                ('safety_level', models.IntegerField(default=1, choices=[(0, b'SAFE'), (1, b'NOT CONFIRMED'), (2, b'UNREACHABLE'), (3, b'NEED_HELP'), (4, b'NOT IN ZONE')])),
                ('retry_count', models.IntegerField(default=0)),
                ('location', models.TextField(null=True)),
                ('comments', models.TextField(null=True)),
                ('status_updated_by', models.TextField(null=True)),
                ('operation', models.ForeignKey(default=None, blank=True, to='operation.Operation')),
            ],
        ),
    ]
