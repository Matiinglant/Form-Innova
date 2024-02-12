# En tu archivo views.py
from django.shortcuts import render, redirect
from .forms import InformacionPersonalForm

def formulario(request):
    if request.method == 'POST':
        form = InformacionPersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario_exitoso')  # Puedes definir una página de éxito
    else:
        form = InformacionPersonalForm()
    return render(request, 'formulario.html', {'form': form})

def formulario_exitoso(request):
    return render(request, 'formulario_exitoso.html')
