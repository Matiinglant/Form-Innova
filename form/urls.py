# En tu archivo urls.py
from django.urls import path
from .views import formulario, formulario_exitoso, vista_datos
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('formulario/', formulario, name='formulario'),
    path('formulario_exitoso/', formulario_exitoso, name='formulario_exitoso'),
  path('vista_datos/', vista_datos, name='vista_datos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
