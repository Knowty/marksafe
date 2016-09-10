# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugee', '0004_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refugee',
            old_name='alternate_contact_number',
            new_name='notification_contact_number',
        ),
        migrations.AlterField(
            model_name='refugee',
            name='safety_level',
            field=models.IntegerField(default=1, choices=[(0, b'SAFE'), (1, b'NOT CONFIRMED'), (2, b'UNREACHABLE'), (3, b'NEED_HELP'), (4, b'NOT IN ZONE')]),
        ),
    ]
