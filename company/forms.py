from django import forms

from .models import Department, Employee

class DateInput(forms.DateInput):
    input_type = 'date'


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('code', 'name',)


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('code', 'name','date_of_birth','gender' ,'dep_id')
        widgets = {
            'date_of_birth': DateInput(),
            }