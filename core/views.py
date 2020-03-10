from django.shortcuts import render, HttpResponse


def ejemplo(request):
    return HttpResponse("<h1>Probando prr</h1>")