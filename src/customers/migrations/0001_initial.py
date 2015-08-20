# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('age', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('height', models.DecimalField(null=True, decimal_places=2, max_digits=5, blank=True)),
                ('weight', models.DecimalField(null=True, decimal_places=2, max_digits=5, blank=True)),
                ('created_date', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='date modified', auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_date', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='date modified', auto_now_add=True)),
                ('shoulder_neck_shoulder', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('top_of_shoulder_to_wrist', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('bicep_under_armpit', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('mid_shoulder', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('low_shoulder', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('front_chest', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('neck_to_jacket_length', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('full_chest_under_armpit', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('stomach', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('hip', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('waist_just_above_belt', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('u_crotch', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('thigh', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('trouser_length', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('trouser_cuff', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('top_of_shoulder_to_fist', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('fist', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('neck_to_shirt_length', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('collar', models.DecimalField(null=True, decimal_places=2, max_digits=6, blank=True)),
                ('customer', models.ForeignKey(to='customers.Customer')),
            ],
        ),
    ]
