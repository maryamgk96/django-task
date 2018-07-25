# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .models import Department, Employee
from .forms import DepartmentForm, EmployeeForm


# Create your views here.
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'company/dep_list.html', {'departments':departments})

def new_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            dep = form.save(commit=False)
            dep.code = request.POST.get('code')
            dep.name = request.POST.get('name')
            dep.save()
            return redirect('department_list')        

    else:
        form = DepartmentForm()
    return render(request, 'company/new_dep.html', {'form': form})


def dept_edit(request, pk):
    dep = Department.objects.get(id=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=dep)
        if form.is_valid():
            dep = form.save(commit=False)
            dep.code = request.POST.get('code')
            dep.name = request.POST.get('name')
            dep.save()
            return redirect('department_list')   
    else:
        form = DepartmentForm(instance=dep)
    return render(request, 'company/new_dep.html', {'form': form})

def dept_delete(request):
    pk=request.GET.get('pk', None)
    dep = Department.objects.get(id=pk)
    dep.delete()
    data={'x':1}
    
    return JsonResponse(data)






def employee_list(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    
    return render(request, 'company/emp_list.html', {'employees':employees,'departments':departments })

def new_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            dep = Department.objects.get(id=request.POST.get('dep_id') )
            emp = form.save(commit=False)
            emp.code = request.POST.get('code')
            emp.name = request.POST.get('name')
            emp.gender = request.POST.get('gender')
            emp.date_of_birth = request.POST.get('date_of_birth')   
            emp.dep_id =  dep                              
            emp.save()
            return redirect('employee_list')        

    else:
        form = EmployeeForm()
    return render(request, 'company/new_emp.html', {'form': form})


def emp_edit(request, pk):
    emp = Employee.objects.get(id=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            dep = Department.objects.get(id=request.POST.get('dep_id') )            
            emp = form.save(commit=False)
            emp.code = request.POST.get('code')
            emp.name = request.POST.get('name')
            emp.gender = request.POST.get('gender')
            emp.date_of_birth = request.POST.get('date_of_birth')   
            emp.dep_id =  dep                               
            emp.save()
            return redirect('employee_list')  
    else:
        form = EmployeeForm(instance=emp)
    return render(request, 'company/new_emp.html', {'form': form})

def emp_delete(request):
    pk=request.GET.get('pk', None)
    emp = Employee.objects.get(id=pk).delete()
    data={'x':1}
    
    return JsonResponse(data)


def emp_by_dep(request,pk):
    # dep = Department.objects.get(id=request.POST.get('dep_id') )
    employees = Employee.objects.filter(dep_id=pk)
    departments = Department.objects.all()
    
    return render(request, 'company/emp_list.html', {'employees':employees,'departments':departments })

               
    
