from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('company/departments', views.department_list, name='department_list'),
    url('comapny/department/create', views.new_department, name='new_department'),
    
]