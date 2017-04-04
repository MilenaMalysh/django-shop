# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_equipment', '0003_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='zoom',
            field=models.IntegerField(default=1),
        ),
    ]
