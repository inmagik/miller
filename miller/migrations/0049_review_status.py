# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0048_auto_20161213_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.CharField(choices=[(b'draft', b'draft'), (b'private', b'private'), (b'public', b'public')], default=b'initial', max_length=8),
        ),
    ]
