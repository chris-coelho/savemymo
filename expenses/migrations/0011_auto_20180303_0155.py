# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0010_auto_20180303_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]