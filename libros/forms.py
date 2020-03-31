from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import Libro, Calificacion, Score

class PuntajeForm(forms.ModelForm):

    class Meta:
        model = Calificacion
        fields = '__all__'
        labels = {
            "usuario": "Usuario",
            "libro": "Libro",
            "puntaje":"Calificacion"
            
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

class ScoreForm(forms.ModelForm):

    class Meta:
        model = Score
        fields = '__all__'
        labels = {
            "usuario": "Usuario",
            "libro": "Libro",
            "valor": "Score"
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
            'valor' : forms.TextInput(
                attrs={
                    'class':'form-control'
                })
        }
        # valor = forms.ChoiceField(required=True,
        #     choices=[(1, 'Si'), (0, 'No')],
        #     widget=forms.Select(
        #         attrs={'class': 'form-control'}
        #         )
        #     )