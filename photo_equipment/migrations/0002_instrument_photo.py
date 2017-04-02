# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_equipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='photo',
            field=models.ImageField(default='ddd.jpg', upload_to='images'),
            preserve_default=False,
        ),
    ]
