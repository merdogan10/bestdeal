# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-25 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestdeal', '0007_auto_20170907_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='affiliate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bestdeal.Affiliate'),
        ),
    ]
