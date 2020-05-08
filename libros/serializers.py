from django.contrib.auth.models import User
from .models import Libro
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'password']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'nombre', 'autor', 'precio', 'editorial', 'nro_paginas', 'url', 'estado']