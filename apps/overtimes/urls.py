from django.urls import path
from .views import (
    OvertimesList, 
    OvertimeCreate,
    OvertimeUpdate,
    OvertimeDelete
)
urlpatterns = [
    path('list', OvertimesList.as_view(), name='list_overtimes'),
    path('novo', OvertimeCreate.as_view(), name='create_overtime'),
    path('update/<int:pk>/', OvertimeUpdate.as_view(), name='update_overtime'),
    path('delete/<int:pk>/', OvertimeDelete.as_view(), name='delete_overtime')
]
