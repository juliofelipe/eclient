from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
    DeleteView
)

from .models import Department

class DepartmentsList(ListView):
    model = Department

    def get_queryset(self):
        company_logger = self.request.user.employee.company
        return Department.objects.filter(company=company_logger)

class DepartmentCreate(CreateView):
    model = Department
    fields = ['name']

    def form_valid(self, form):
        department = form.save(commit=False)
        department.company = self.request.user.employee.company
        department.save()
        return super(DepartmentCreate, self).form_valid(form)

class DepartmentUpdate(UpdateView):
    model = Department
    fields = ['name']

class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('list_departments')