# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=50)),
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
