# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Refugee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=b'refugee_photos', blank=True)),
                ('alternate_contact_number', models.CharField(max_length=20, blank=True)),
                ('safety_level', models.IntegerField(choices=[(0, b'SAFE'), (1, b'UNREACHABLE'), (2, b'NEED_HELP')])),
                ('location', models.TextField()),
            ],
        ),
    ]
