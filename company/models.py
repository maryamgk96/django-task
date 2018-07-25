# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Department(models.Model):
    code = models.DecimalField(max_digits=3, decimal_places=0,unique=True)
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Employee(models.Model):
    code = models.DecimalField(max_digits=6, decimal_places=0,unique=True)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    gender_choices=(
        ('male', 'Male'),
        ('female', 'Female'),
        
    )
    gender = models.CharField(max_length=6,
                            choices = gender_choices,
                                default='female')
    dep_id = models.ForeignKey(Department)


    def __str__(self):
        return self.name