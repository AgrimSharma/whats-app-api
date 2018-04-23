# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180423_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='jewellery',
            name='product_type',
            field=models.CharField(max_length=100, default=""),
            preserve_default=False,
        ),
    ]
