from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import Libro, Calificacion

class PuntajeForm(BSModalForm):

    class Meta:
        model = Calificacion
        fields = '__all__'
        widgets = {
            'puntaje' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }