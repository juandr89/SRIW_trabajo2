from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Libro , Calificacion
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
        print(context)
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