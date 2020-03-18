from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Libro , Calificacion
from django.contrib.auth.models import User
from .forms import PuntajeForm

# Create your views here.

@method_decorator([login_required], name='dispatch')
class VerLibros(ListView):
    model = Libro
    context_object_name = 'libros_list'
    template_name = 'libros/libros.html'

    def get_context_data(self, **kwargs):
        context = super(VerLibros, self).get_context_data(**kwargs)
        context['calificaciones_list'] = Calificacion.objects.all()
        return context

@method_decorator([login_required], name='dispatch')
class ModificarCalificacion(UpdateView):
    model = Calificacion
    form_class = PuntajeForm
    template_name_suffix = '_update_form'
    success_url =  reverse_lazy('libros')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        messages.success(request, 'Calificación modificada')
        return super(ModificarCalificacion, self).post(request, kwargs)


@method_decorator([login_required], name='dispatch')
class VerPerfilUsuario(TemplateView, ):
    template_name = 'libros/perfil-usuario.html'

    def get_user_profile(self, user):
        # Número de características
        attr = 2
        calificaciones = Calificacion.objects.filter(usuario = user)
        list_libros = []
        for c in calificaciones:
            list_libros.append(c.libro)

        mat = []
        sumaCalificaciones = 0
        for i in range(len(list_libros)):
            cal = Calificacion.objects.filter(usuario = user, libro = list_libros[i])[0].puntaje
            sumaCalificaciones += cal
            row = []
            for j in range(attr):
                if j == 0:
                    value = list_libros[i].nro_paginas
                else:
                    value = list_libros[i].precio
                row.append(cal * value)
            mat.append(row)

        rowSuma = []
        for i in range(attr):
            suma = 0
            for j in range(len(mat)):
                suma += mat[j][i]
            rowSuma.append(suma)

        perfil = []
        for i in range(len(rowSuma)):
            perfil.append(round((rowSuma[i]/sumaCalificaciones), 3))

        obj = {'nro_paginas': perfil[0], 'precio': perfil[1]}
        return obj

    def get_context_data(self, **kwargs):
        context = super(VerPerfilUsuario, self).get_context_data(**kwargs)
        context['perfil'] = self.get_user_profile(self.request.user)
        return context