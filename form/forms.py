from django import forms
from .models import InformacionPersonal

class InformacionPersonalForm(forms.ModelForm):
    RESPUESTAS = [
        ('', 'Seleccione'),
        ('Si', 'Si'),
        ('No', 'No'),
    ]
    tiene_cortes_energia = forms.ChoiceField(label='¿Tiene cortes de energía de forma seguida?', choices=RESPUESTAS, required=False)
    tiene_internet = forms.ChoiceField(label='¿Tiene internet en casa?', choices=RESPUESTAS, required=False)
    tiene_computadora = forms.ChoiceField(label='¿Posee una computadora?', choices=RESPUESTAS, required=False)
    computadora_funciona = forms.ChoiceField(label='¿La computadora funciona?', choices=RESPUESTAS, required=False)
    tiene_telefono_propio = forms.ChoiceField(label='¿Tiene teléfono propio?', choices=RESPUESTAS, required=False)
    conocimientos_programacion = forms.ChoiceField(label='¿Tiene conocimientos de programación?', choices=RESPUESTAS, required=False)
    archivos_1 = forms.FileField(label='Certificado de Idiomas(Opcional)', required=False)
    archivos_2 = forms.FileField(label='Certificados de Programación(Opcional)', required=False)
    archivos_3 = forms.FileField(label='Referencias Laborales(Opcional)', required=False)
    class Meta:
        model = InformacionPersonal
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'correo_electronico', 'numero_telefono', 'provincia', 'localidad', 'tiene_cortes_energia', 'tiene_internet', 'tiene_computadora', 'computadora_funciona', 'tiene_telefono_propio', 'conocimientos_programacion', 'archivos_1', 'archivos_2', 'archivos_3']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'format': 'dd-mm-YYYY'})
        }