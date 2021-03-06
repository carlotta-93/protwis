# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-02 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0002_auto_20170908_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='proteinsegment',
            name='proteinfamily',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proteinsegment',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='proteinsegment',
            unique_together=set([('slug', 'proteinfamily')]),
        ),
    ]
