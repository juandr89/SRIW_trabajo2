from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .models import Libro , Calificacion
from django.contrib.auth.models import User
from .forms import PuntajeForm

# Functions
from .functions import get_user_profile, get_recomendations

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
class CrearCalificacion(CreateView):
    model = Calificacion
    form_class = PuntajeForm
    template_name_suffix = '_create_form'
    success_url =  reverse_lazy('ver_libros')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        messages.success(request, 'Calificación creada')
        return super(CrearCalificacion, self).post(request, kwargs)

@method_decorator([login_required], name='dispatch')
class ModificarCalificacion(UpdateView):
    model = Calificacion
    form_class = PuntajeForm
    #template_name_suffix = '_update_form'
    template_name = 'libros/calificacion_update_form.html'
    success_url =  reverse_lazy('ver_libros')
    
    def get_queryset(self):
        current_user = self.request.user.id

    def get_object(self):
        id_libro = self.kwargs['pk']
        return get_object_or_404(Calificacion, libro=id_libro)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        messages.success(request, 'Calificación modificada')
        return super(ModificarCalificacion, self).post(request, kwargs)


@method_decorator([login_required], name='dispatch')
class VerPerfilUsuario(TemplateView):
    template_name = 'libros/perfil-usuario.html'

    def get_context_data(self, **kwargs):
        context = super(VerPerfilUsuario, self).get_context_data(**kwargs)
        if len(Calificacion.objects.filter(usuario = self.request.user)) != 0:
            context['perfil'] = get_user_profile(self.request.user)
        return context

@method_decorator([login_required], name='dispatch')
class VerRecomendaciones(ListView):
    model = Libro
    template_name = 'libros/recomendaciones.html'

    def get_context_data(self, **kwargs):
        context = super(VerRecomendaciones, self).get_context_data(**kwargs)
        context['recomendaciones'] = get_recomendations(self.request.user)
        return context