# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=10)),
                ('lName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30, unique=True)),
            ],
        ),
    ]
