# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
    ]
