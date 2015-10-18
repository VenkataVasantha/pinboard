# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('blurb', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('thumbnail', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
            ],
        ),
    ]
