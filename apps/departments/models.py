from django.db import models
from apps.companies.models import Company
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=70)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('list_departments')

    def __str__(self):
        return self.name

