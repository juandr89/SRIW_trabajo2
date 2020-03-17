from django.urls import path

from .views import VerLibros, ModificarCalificacion

urlpatterns = [
    path('ver_libros/', VerLibros.as_view(), name='ver_libros'),
    path('modificar-calificacion/<int:pk>', ModificarCalificacion.as_view(), name='modificar-calificacion')
]