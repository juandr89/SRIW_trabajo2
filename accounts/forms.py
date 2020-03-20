from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import datetime

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label='Primer nombre', max_length=40, min_length=2, required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'autofocus': 'autofocus', 'id': '2dasd'}
        )
    )
    # Username es con lo que se va a logear, que en este caso lo vamos a tratar como el correo
    username = forms.EmailField(
        label='Correo',  max_length=25, min_length=5, required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    password1 = forms.CharField(
        label='Contraseña', required=True, max_length=40, min_length=6,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    def clean_username(self):
        id = self.cleaned_data['username']
        temp = User.objects.filter(username=id).count()
        if temp>0:
            raise forms.ValidationError("Ya existe un usuario registrado con esa identificación.")
        return id

    class Meta:
        model = User
        fields = [
            'first_name', 'username', 'password1'
            ]

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Email', required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': 'autofocus'
                }
        )
    )
    password = forms.CharField(
        label='Contraseña', required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña'}
        )
    )