# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20171031_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(default='static/assets/no-img.png', upload_to='static/assets/'),
        ),
    ]