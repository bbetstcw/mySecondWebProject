# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooncakeTestEnvironment', '0012_add_metadata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meta_data',
            old_name='metat_keywords',
            new_name='meta_keywords',
        ),
    ]
