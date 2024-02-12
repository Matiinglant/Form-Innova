# En tu archivo urls.py principal

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form.urls')),  # Reemplaza 'tu_app' con el nombre de tu aplicación
]
