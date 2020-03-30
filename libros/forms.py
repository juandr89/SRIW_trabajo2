from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import Libro, Calificacion

class PuntajeForm(forms.ModelForm):

    class Meta:
        model = Calificacion
        fields = '__all__'
        labels = {
            "usuario": "Usuario",
            "libro": "Libro",
            "puntaje": "Puntaje",
            
        }
        widgets = {
            'usuario' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }),
            'libro' : forms.TextInput(
                attrs={
                    'class':'form-control'
                }),
            'puntaje' : forms.TextInput(
                attrs={
                    'class':'form-control'
                })
        }