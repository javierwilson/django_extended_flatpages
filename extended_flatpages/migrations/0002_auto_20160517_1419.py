# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extended_flatpages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cmsflatpage',
            options={'verbose_name': 'CMS Flat Pages'},
        ),
        migrations.RemoveField(
            model_name='cmsflatpage',
            name='id',
        ),
        migrations.AlterField(
            model_name='cmsflatpage',
            name='page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='flatpages.FlatPage', verbose_name='Page'),
        ),
    ]
