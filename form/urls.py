# En tu archivo urls.py
from django.urls import path
from .views import formulario, formulario_exitoso

urlpatterns = [
    path('formulario/', formulario, name='formulario'),
    path('formulario_exitoso/', formulario_exitoso, name='formulario_exitoso'),
]
