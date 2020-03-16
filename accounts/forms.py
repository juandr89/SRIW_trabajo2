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
    last_name = forms.CharField(
        label='Primer apellidos',  max_length=40, min_length=2, required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    # Username es con lo que se va a logear, que en este caso lo vamos a tratar como la identificacion
    username = forms.CharField(
        label='Identificacion',  max_length=15, min_length=5, required=True,
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
    password2 = forms.CharField(
        label='Verificar contraseña', required=True, max_length=40, min_length=6,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        label='Correo electrónico', required=True, max_length=40,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
                }
        )
    )

    def email(self):
        correo = self.cleaned_data['email']
        temp = User.objects.filter(email=correo).count()
        if temp>0:
            raise forms.ValidationError("Ya existe un usuario registrado con ese correo.")
        return correo

    def name(self):
        id = self.cleaned_data['name']
        temp = User.objects.filter(name=name).count()

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username',
            'password1', 'password2', 'email',
            ]

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Identificacion', required=True,
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