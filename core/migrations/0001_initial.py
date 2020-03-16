# Generated by Django 3.0.4 on 2020-03-15 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('autor', models.CharField(blank=True, max_length=80, null=True)),
                ('editorial', models.CharField(blank=True, max_length=100, null=True)),
                ('nro_paginas', models.IntegerField(blank=True, null=True)),
                ('precio', models.FloatField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=500, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=500, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.FloatField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Libro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
