# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-29 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0003_auto_20161027_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='proteinsegment',
            name='proteinfamily',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
