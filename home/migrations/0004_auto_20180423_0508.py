# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_jewellery_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jewellery',
            name='tags',
            field=models.CharField(max_length=1000, default=''),
        ),
        migrations.AlterField(
            model_name='jewellery',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
