# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 23:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_userprofile_favorite_topics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='favoritetopics',
            old_name='userprofile',
            new_name='profile',
        ),
    ]