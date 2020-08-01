from django.urls import path
from .views import  (
    EmployeesList, 
    EmployeeEdit, 
    EmployeeDelete, 
    EmployeeCreate
)

urlpatterns = [
    path('list', EmployeesList.as_view(), name='list_employees'),
    path('novo/', EmployeeCreate.as_view(), name='create_employee'),
    path('editar/<int:pk>/', EmployeeEdit.as_view(), name='update_employee'),
    path('apagar/<int:pk>/', EmployeeDelete.as_view(), name='delete_employee')
]
