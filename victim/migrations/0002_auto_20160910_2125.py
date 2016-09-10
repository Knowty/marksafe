# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('victim', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='victim',
            old_name='comments',
            new_name='additional_information',
        ),
        migrations.RemoveField(
            model_name='victim',
            name='photo',
        ),
    ]
