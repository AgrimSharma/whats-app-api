# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jewellery',
            options={'verbose_name_plural': 'Jewellery', 'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='jewellery',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
