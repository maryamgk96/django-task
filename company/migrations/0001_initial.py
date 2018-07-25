# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.DecimalField(unique=True, max_digits=3, decimal_places=0)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.DecimalField(unique=True, max_digits=6, decimal_places=0)),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(default='female', max_length=6, choices=[('male', 'Male'), ('female', 'Female')])),
                ('dep_id', models.ForeignKey(to='company.Department')),
            ],
        ),
    ]
