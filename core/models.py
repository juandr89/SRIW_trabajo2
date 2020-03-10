from django.db import models
from django.contrib.auth.models import User, Permission


class Libro(models.Model):
    nombre = models.CharField(max_length=80)
    autor = models.CharField(max_length=80, null=True, blank=True)
    editorial = models.CharField(max_length=100, null=True, blank=True)
    nro_paginas = models.IntegerField(null=True, blank=True)
    precio = models.FloatField(null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    observaciones = models.CharField(max_length=500, null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Calificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT)
    puntaje = models.FloatField()

    def __str__(self):
        return f"libro: {self.libro} - calificacion {self.puntaje}"