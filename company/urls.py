from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('company/departments/$', views.department_list, name='department_list'),
    url('comapny/department/create/$', views.new_department, name='new_department'),
    url('comapny/department/(?P<pk>\d+)/edit/$', views.dept_edit, name='dept_edit'),   
    url(r'^comapny/department/$', views.dept_delete, name='dept_delete'),

    url('company/employees/$', views.employee_list, name='employee_list'),
    url('comapny/employee/create/$', views.new_employee, name='new_employee'),
    url('comapny/employee/(?P<pk>\d+)/edit/$', views.emp_edit, name='emp_edit'),   
    url(r'^comapny/employee/$', views.emp_delete, name='emp_delete'),
    url('/company/department/(?P<pk>\d+)/$',views.emp_by_dep, name='emp_by_dep')
 
    
]