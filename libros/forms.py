from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import Libro, Calificacion, Score

class PuntajeForm(forms.ModelForm):

    class Meta:
        model = Calificacion
        fields = ('puntaje',)
        labels = {
            "puntaje":"Calificacion"
            
        }
        widgets = {
            'puntaje' : forms.TextInput(
                attrs={
                    'class':'form-control'
                })
        }

class ScoreForm(forms.ModelForm):

    class Meta:
        model = Score
        fields = ('valor',)
        labels = {
            "valor": "Score"
        }
        widgets = {
            'valor' : forms.TextInput(
                attrs={
                    'class':'form-control'
                })
        }