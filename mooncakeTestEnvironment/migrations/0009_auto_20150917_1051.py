# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooncakeTestEnvironment', '0008_remove_marketing_content_from_navigation'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('metat_keywords', models.TextField()),
                ('meta_description', models.TextField()),
                ('service', models.ForeignKey(to='mooncakeTestEnvironment.Service')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='metadata',
            unique_together=set([('service',)]),
        ),
    ]
