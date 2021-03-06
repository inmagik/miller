# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0056_auto_20161215_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='category',
            field=models.CharField(choices=[(b'editing', b'editing'), (b'double', b'double blind'), (b'open', b'open')], default=b'editing', max_length=8),
        ),
        migrations.AlterField(
            model_name='review',
            name='contents',
            field=models.TextField(blank=True, default=b'{\n "text": "", \n "title": ""\n}'),
        ),
    ]
