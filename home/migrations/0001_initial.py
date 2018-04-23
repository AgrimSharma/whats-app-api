# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jewellery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.URLField()),
                ('status', models.BooleanField()),
                ('created', models.DateField(default=datetime.date(2018, 4, 23))),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
