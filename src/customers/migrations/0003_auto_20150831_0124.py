# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20150828_0634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstripe',
            name='user',
        ),
        migrations.AddField(
            model_name='customer',
            name='stripe_account',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.DeleteModel(
            name='UserStripe',
        ),
    ]
