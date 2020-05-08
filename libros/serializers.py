from django.contrib.auth.models import User
from .models import Libro
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Contraseña'}
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'password']
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'nombre', 'autor', 'precio', 'editorial', 'nro_paginas', 'url', 'estado']