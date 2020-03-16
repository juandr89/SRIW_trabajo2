import datetime as dt
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class CrearUsuario(CreateView):
    template_name = 'accounts/signup.html'
    model = User
    form_class = SignUpForm
    success_url =  reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        post = request.POST.copy()
        form = self.form_class(post)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = form.save()
            user.usuario.email = form.cleaned_data['email']
            user.save()
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('home')
        else:
            messages.error(request, 'Fallo en el registro')
        return render(request, 'accounts/signup.html', {'form': form})