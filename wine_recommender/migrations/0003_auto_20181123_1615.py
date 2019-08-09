# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-23 10:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wine_recommender', '0002_cluster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]