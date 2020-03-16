from django.contrib import admin
from .models import Libro, Calificacion

# Register your models here.
admin.site.register(Libro)
admin.site.register(Calificacion)