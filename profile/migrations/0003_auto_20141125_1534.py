# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20141125_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(default=b'text', max_length=10, choices=[(b'EMAIL', b'email'), (b'TEXT', b'text')]),
            preserve_default=True,
        ),
    ]
