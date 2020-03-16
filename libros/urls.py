from django.urls import path

from .views import VerLibros, ModificarCalificacion

urlpatterns = [
    path('libros/', VerLibros.as_view(), name='libros'),
    path('modificar-calificacion/<int:pk>', ModificarCalificacion.as_view(), name='modificar-calificacion')
]