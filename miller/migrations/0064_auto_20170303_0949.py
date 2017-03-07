# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-03 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0063_comment_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[(b'pending', b'pending acceptation'), (b'private', b'accepted, privately visible'), (b'on review', b'from reviewer'), (b'public', b'accepted, publicly visible'), (b'deleted', b'deleted')], db_index=True, default=b'private', max_length=10),
        ),
    ]