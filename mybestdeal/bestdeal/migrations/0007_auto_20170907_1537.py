# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestdeal', '0006_ads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='category',
        ),
        migrations.AddField(
            model_name='ads',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bestdeal.Sub_Category'),
        ),
    ]
