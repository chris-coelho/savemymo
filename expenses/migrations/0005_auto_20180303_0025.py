# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 00:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_auto_20180303_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.CharField(default='d90e7183bf994a2181fd0205de63562c', max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='expense',
            name='register_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]