# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Department(models.Model):
    code = models.PositiveIntegerField( validators=[
            MaxValueValidator(3)
        ])
    name = models.TextField()


    def __str__(self):
        return self.name


class Employee(models.Model):
    code = models.PositiveIntegerField( validators=[
            MaxValueValidator(6)
        ])
    name = models.TextField()
    date_of_birth = models.DateField(blank=True, null=True)
    gender=(
        ('male', 'Male'),
        ('female', 'Female')
        
    )
    dep_id = models.ForeignKey(Department)


    def __str__(self):
        return self.name