from django.urls import path

from .views import VerLibros, ModificarCalificacion, VerPerfilUsuario

urlpatterns = [
    path('ver_libros/', VerLibros.as_view(), name='ver_libros'),
    path('modificar-calificacion/<int:pk>', ModificarCalificacion.as_view(), name='modificar-calificacion'),
    path('perfil-usuario/', VerPerfilUsuario.as_view(), name='perfil-usuario'),
]