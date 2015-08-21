# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('clas', models.CharField(default='fighter', max_length=20, choices=[('fighter', 'fighter'), ('wizard', 'wizard'), ('healer', 'healer')])),
                ('hp', models.IntegerField()),
                ('st', models.IntegerField()),
                ('df', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('max_characters', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='game',
            field=models.ForeignKey(to='lobby.Game'),
        ),
    ]
