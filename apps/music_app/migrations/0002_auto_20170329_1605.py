# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 21:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artist',
            new_name='album',
        ),
    ]
