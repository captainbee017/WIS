# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='common.Location')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_type', models.CharField(choices=[('Mobile', 'Mobile'), ('Home', 'Home'), ('Work', 'Work')], default='Mobile', max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='customer.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
