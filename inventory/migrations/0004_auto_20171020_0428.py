# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 04:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20171018_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcategory',
            old_name='category',
            new_name='name',
        ),
    ]
