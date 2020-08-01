from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
    DeleteView
)

from .models import Overtime
from .forms import OvertimeForm

class OvertimesList(ListView):
    model = Overtime

    def get_queryset(self):
        company_logger = self.request.user.employee.company
        return Overtime.objects.filter(employee__company=company_logger)

class OvertimeUpdate(UpdateView):
    model = Overtime
    fields = ['reason', 'employee', 'hours']

class OvertimeDelete(DeleteView):
    model = Overtime
    success_url = reverse_lazy('list_overtimes')

class OvertimeCreate(CreateView):
    model = Overtime
    form_class = OvertimeForm

    def get_form_kwargs(self):
        kwargs = super(OvertimeCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    