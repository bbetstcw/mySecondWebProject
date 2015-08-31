# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooncakeTestEnvironment', '0002_addDataToTables'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_link',
            name='image_title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
