# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooncakeTestEnvironment', '0010_add_mata_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta_data',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('metat_keywords', models.TextField()),
                ('meta_description', models.TextField()),
                ('service', models.ForeignKey(to='mooncakeTestEnvironment.Service')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='metadata',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='service',
        ),
        migrations.DeleteModel(
            name='MetaData',
        ),
        migrations.AlterUniqueTogether(
            name='meta_data',
            unique_together=set([('service',)]),
        ),
    ]
