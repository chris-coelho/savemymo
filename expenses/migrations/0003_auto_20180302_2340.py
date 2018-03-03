# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20180302_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='register_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.CharField(default='0c78dfe8bc0e49419bec0055b9891c76', max_length=32, primary_key=True, serialize=False),
        ),
    ]