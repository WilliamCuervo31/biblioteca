from django.shortcuts import render, redirect
from user.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from readConRitmo import urls
from django.contrib import messages
from core.models import *
from core.utils.trees import LibroBST

def index(request):
    return render(request, 'html/index.html')

def consultaLibros(request):
    
    arbol = LibroBST()

    libros = Libros.objects.all()
    for l in libros:
        arbol.insertar(l)

    libros_ordenados = arbol.in_order()

    return render(request, '', {
        'libros': libros_ordenados
    })

def crearEtiqueta(request):
    etiquetas = Etiqueta.objects.all()

    if request.method == "GET" and request.GET.get("nombre"):
        data = request.GET
        padre_id = data.get("padre")
        padre = None

        if padre_id:
            try:
                padre = Etiqueta.objects.get(id=padre_id)
            except Etiqueta.DoesNotExist:
                padre = None

        etiqueta_nueva = Etiqueta.objects.create(
            nombre = data.get('nombre'),
            descripcion = data.get('descripcion'),
            color = data.get('color'),
            activo = True,
            padre = padre
        )

        messages.success(request, f"✅ Se creó correctamente la etiqueta {etiqueta_nueva.nombre}")
        return redirect('lista_etiquetas')

    return render(request, 'crear_etiqueta.html', {'etiquetas': etiquetas})
