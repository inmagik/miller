# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-21 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0061_auto_20170203_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='highlights',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[(b'bibtex', b'bibtex'), (b'crossref', b'bibtex'), (b'video-cover', b'video interview'), (b'video', b'video'), (b'text', b'text'), (b'picture', b'picture'), (b'pdf', b'pdf'), (b'image', b'image'), (b'photo', b'photo'), (b'rich', b'rich'), (b'link', b'link'), (b'audiovisual', b'audiovisual')], max_length=24),
        ),
    ]
