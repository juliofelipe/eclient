from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.views.generic import (
    ListView, 
    UpdateView, 
    DeleteView, 
    CreateView
)

from .models import Employee


class EmployeesList(ListView):
    model = Employee

    def get_queryset(self):
        company_logged = self.request.user.employee.company
        return Employee.objects.filter(company=company_logged)

class EmployeeEdit(UpdateView):
    model = Employee
    fields = ['name', 'departments']

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('list_employees')

class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'departments']
    
    def form_valid(self, form):
        employee = form.save(commit=False)
        username = employee.name.split(' ')[0] + employee.name.split(' ')[1]
        employee.company = self.request.user.employee.company
        employee.user = User.objects.create(username=username)
        employee.save()
        return super(EmployeeCreate, self).form_valid(form)
        