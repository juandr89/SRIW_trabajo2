from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import datetime

class SignUpForm(UserCreationForm):
    fisrt_name = forms.CharField(
        label='Primer nombre', max_length=20, min_length=2, required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'autofocus': 'autofocus', 'id': '2dasd'}
        )
    )
    email, username = forms.EmailField(
        label='Correo electrónico', required=True, max_length=25,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
                }
        )
    )
    password = forms.CharField(
        label='Contraseña', required=True, max_length=20, min_length=6,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
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
            'name', 'email', 'password'
            ]

class LoginForm(AuthenticationForm):
    email = forms.CharField(
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