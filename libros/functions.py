import numpy as np
import math

from .models import Libro , Calificacion

# get values user profile
def get_user_profile(user):

    autores = []
    editoriales = []
    libros_all = Libro.objects.filter()
    for l in libros_all:
        if not (l.autor in autores):
            autores.append(l.autor)
        if not (l.editorial in editoriales):
            editoriales.append(l.editorial)

    calificaciones = Calificacion.objects.filter(usuario = user)
    list_libros = []
    for c in calificaciones:
        list_libros.append(c.libro)

    labels = ['nro_paginas', 'precio']
    for i in autores:
        labels.append(i)
    for i in editoriales:
        labels.append(i)

    # aux = get_mat_user(user, list_libros, labels)
    # mat = aux[0]
    # sumaCalificaciones = aux[1]

    mat = []
    sumaCalificaciones = 0
    for i in range(len(list_libros)):
        cal = Calificacion.objects.filter(usuario = user, libro = list_libros[i])[0].puntaje
        aut = Calificacion.objects.filter(usuario = user, libro = list_libros[i])[0].libro.autor
        ed = Calificacion.objects.filter(usuario = user, libro = list_libros[i])[0].libro.editorial
        sumaCalificaciones += cal
        row = []
        for j in range(len(labels)):
            if j == 0:
                value = list_libros[i].nro_paginas * cal
            elif j == 1:
                value = list_libros[i].precio * cal
            else:
                if labels[j] == aut or labels[j] == ed:
                    value = cal
                else:
                    value = 0
            row.append(value)
        mat.append(row)

    rowSuma = []
    for i in range(len(labels)):
        suma = 0
        for j in range(len(mat)):
            suma += mat[j][i]
        rowSuma.append(suma)

    perfil = []
    for i in range(len(rowSuma)):
        if i == 0 or i == 1:
            perfil.append(round((rowSuma[i]/sumaCalificaciones), 3))
        else:
            if i > 1 and i < len(autores) + 2:
                sumAux = sum(rowSuma[2:len(autores) + 2])
                perfil.append(round((rowSuma[i]/sumAux), 3))
            else:
                sumAux = sum(rowSuma[len(autores) + 2: len(labels)])
                perfil.append(round((rowSuma[i]/sumAux), 3))

    listaPerfil = []
    for i in range(len(labels)):
        obj = {'label': labels[i], 'value': perfil[i]}
        listaPerfil.append(obj)
    return listaPerfil

# get profile user normalize
def get_user_profile_normalize(user):

    autores = []
    editoriales = []
    libros_all = Libro.objects.filter()
    for l in libros_all:
        if not (l.autor in autores):
            autores.append(l.autor)
        if not (l.editorial in editoriales):
            editoriales.append(l.editorial)
    
    calificaciones = Calificacion.objects.filter(usuario = user)
    list_libros = []
    for c in calificaciones:
        list_libros.append(c.libro)
        
    labels = ['nro_paginas', 'precio']
    for i in autores:
        labels.append(i)
    for i in editoriales:
        labels.append(i)
    
    mat = []
    sumaCalificaciones = 0
    for i in range(len(list_libros)):
        cal = Calificacion.objects.filter(usuario = user, libro = list_libros[i])[0].puntaje
        aut = Calificacion.objects.filter(usuario = user, libro = list_libros[i])[0].libro.autor
        ed = Calificacion.objects.filter(usuario = user, libro = list_libros[i])[0].libro.editorial
        sumaCalificaciones += cal
        row = []
        for j in range(len(labels)):
            if j == 0:
                value = list_libros[i].nro_paginas 
            elif j == 1:
                value = list_libros[i].precio
            else:
                if labels[j] == aut or labels[j] == ed:
                    value = cal
                else:
                    value = 0
            row.append(value)
        mat.append(row)

    profile = get_user_profile(user)

    matNp = np.matrix(mat) 
    maxValues = np.squeeze(np.asarray(matNp.max(0)))
    minValues = np.squeeze(np.asarray(matNp.min(0)))

    for i in range(2):
        value = profile[i]['value']
        value = (value-minValues[i])/(maxValues[i]-minValues[i])
        profile[i]['value'] = round(value, 3)

    return profile

# get recomendations
def get_recomendations_content(user):
    profile = get_user_profile_normalize(user)

    autores = []
    editoriales = []
    libros_all = Libro.objects.filter()
    for l in libros_all:
        if not (l.autor in autores):
            autores.append(l.autor)
        if not (l.editorial in editoriales):
            editoriales.append(l.editorial)

    list_libros = []
    for l in libros_all:
        if len(Calificacion.objects.filter(usuario = user, libro = l)) == 0:
            list_libros.append(l)

    labels = ['nro_paginas', 'precio']
    for i in autores:
        labels.append(i)
    for i in editoriales:
        labels.append(i)
    
    mat = []
    auxx = []
    for i in range(len(list_libros)):
        aut = list_libros[i].autor
        ed = list_libros[i].editorial
        row = []
        for j in range(len(labels)):
            if j == 0:
                value = list_libros[i].nro_paginas 
            elif j == 1:
                value = list_libros[i].precio
            else:
                if labels[j] == aut or labels[j] == ed:
                    auxx.append(labels[j])
                    value = 1
                else:
                    value = 0
            row.append(value)
        mat.append(row)

    # Normalize precio and nro_paginas
    matNp = np.matrix(mat) 
    maxValues = np.squeeze(np.asarray(matNp.max(0)))
    minValues = np.squeeze(np.asarray(matNp.min(0)))

    for i in range(len(mat)):
        for j in range(2):
            value = mat[i][j]
            value = (value-minValues[j])/(maxValues[j]-minValues[j])
            mat[i][j] = value

    valuesNorm = []
    for i in profile:
        valuesNorm.append(i['value'])
    
    puntajeEuc = []
    for i in mat:
        suma = 0
        for j in range(len(i)):
            suma += pow((valuesNorm[j] -  i[j]), 2)
        puntajeEuc.append(math.sqrt(suma))

    lista = []
    for i in range(len(list_libros)):
        lista.append((list_libros[i], puntajeEuc[i]))

    listaOrdenada = sorted(lista, key=lambda tup: tup[1])
    recomendacion = []
    for i in listaOrdenada:
        recomendacion.append(i[0])

    return recomendacion

def get_recomendations_colab(user):
    # TODO: Recomendación colaborativa. Retorna una lista con los libros a recomendar (ordenada)
    return 0

# Estrategia basada en la popularidad: recomendar los productos más populares
def coldStartUser():
    calificaciones = Calificacion.objects.filter()

    list_libros = []
    for c in calificaciones:
        if not c.libro in list_libros:
            list_libros.append(c.libro)
    
    popularidad = []
    for l in list_libros:
        cal = Calificacion.objects.filter(libro = l)
        sumaCal = 0
        for c in cal:
            sumaCal += c.puntaje
        promCal = sumaCal/len(cal)
        popularidad.append((l, promCal))
    
    listaOrdenada = sorted(popularidad, key=lambda tup: tup[1], reverse=True)
    recomendacion = []
    for i in listaOrdenada:
        recomendacion.append(i[0])
    
    if len(recomendacion) > 10:
        recomendacion = recomendacion[:10]
    
    return recomendacion

def get_recomendations(user):
    pesoContenido = 0.6
    pesoColaborativo = 0.4

    #Cold Start (User) - https://medium.com/@juancarlosjaramillo_88910/gu%C3%ADa-para-construir-un-sistema-de-recomendaci%C3%B3n-parte-1-2b1a65d6eac3
    if len(Calificacion.objects.filter(usuario = user)) == 0:
        listCon = coldStartUser()
    else: 
        listCon = get_recomendations_content(user)
        # listCol = get_recomendations_colab(user)

        # TODO: Sistema híbrido
    
    return listCon