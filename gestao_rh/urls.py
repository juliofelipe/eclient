from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('employees/', include('apps.employees.urls')),
    path('departments/', include('apps.departments.urls')),
    path('company/', include('apps.companies.urls')),
    path('document/', include('apps.documents.urls')),
    path('overtimes/', include('apps.overtimes.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
