# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='refugee',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='refugee',
            name='operation',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='refugee',
            name='status_updated_by',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='refugee',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='refugee',
            name='safety_level',
            field=models.IntegerField(default=1, choices=[(0, b'SAFE'), (1, b'NOT CONFIRMED'), (2, b'UNREACHABLE'), (3, b'NEED_HELP'), (4, b'NOT IN ZONE')]),
        ),
    ]
