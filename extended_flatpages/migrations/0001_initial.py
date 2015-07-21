# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSFlatPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=350, verbose_name='Description')),
                ('keywords', models.CharField(max_length=200, verbose_name='Keywords')),
                ('page', models.OneToOneField(verbose_name='Page', to='flatpages.FlatPage')),
            ],
        ),
    ]
