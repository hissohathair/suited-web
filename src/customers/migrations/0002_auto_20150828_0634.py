# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStripe',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('stripe_id', models.CharField(max_length=200, blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
    ]
