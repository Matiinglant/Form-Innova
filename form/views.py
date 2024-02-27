from django.shortcuts import render, redirect
from .forms import InformacionPersonalForm
from .models import InformacionPersonal
def formulario(request):
    if request.method == 'POST':
        form = InformacionPersonalForm(request.POST, request.FILES    )
        if form.is_valid():
            form.save()
            return redirect('formulario_exitoso')  # Puedes definir una página de éxito
    else:
        form = InformacionPersonalForm()
    return render(request, 'formulario.html', {'form': form})

def formulario_exitoso(request):
    return render(request, 'formulario_exitoso.html')

def vista_datos(request):
    datos = InformacionPersonal.objects.all()
    return render(request, 'vista_datos.html', {'datos': datos})