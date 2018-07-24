# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Department, Employee
from .forms import DepartmentForm


# Create your views here.
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'company/dep_list.html', {'departments':departments})

def new_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            dep = form.save(commit=False)
            dep.code = request.code
            dep.name = request.name
            dep.save()
            return redirect('department_list')        

    else:
        form = DepartmentForm()
        return render(request, 'company/new_dep.html', {'form': form})
