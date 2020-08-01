from django.urls import path
from .views import (
    DepartmentsList, 
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentDelete
)
urlpatterns = [
    path('list', DepartmentsList.as_view(), name='list_departments'),
    path('novo', DepartmentCreate.as_view(), name='create_department'),
    path('update/<int:pk>/', DepartmentUpdate.as_view(), name='update_department'),
    path('delete/<int:pk>/', DepartmentDelete.as_view(), name='delete_department')
]
