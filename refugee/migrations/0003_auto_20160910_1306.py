# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugee', '0002_auto_20160910_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='refugee',
            name='retry_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='refugee',
            name='operation',
            field=models.ForeignKey(default=None, blank=True, to='operation.Operation'),
        ),
    ]
