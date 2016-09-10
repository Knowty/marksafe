# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refugee',
            name='phone_number',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='refugee',
            name='safety_level',
            field=models.IntegerField(default=1, choices=[(0, b'SAFE'), (1, b'NOT CONFIRMED'), (2, b'UNREACHABLE'), (3, b'NEED_HELP')]),
        ),
    ]
