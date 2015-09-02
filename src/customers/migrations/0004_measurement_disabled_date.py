# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20150831_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='disabled_date',
            field=models.DateTimeField(null=True, verbose_name='date disabled', blank=True),
        ),
    ]
