from django.shortcuts import render, redirect
from user.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from readConRitmo import urls
from .utils import obtener_descendientes
from django.contrib import messages
from core.models import *
from core.utils.trees import LibroBST

def index(request):
    return render(request, 'html/index.html')

def consultaLibros(request):
    orden = request.GET.get("orden", "asc")
    etiquetas = request.GET.getlist("etiquetas")

    libros = Libros.objects.all()

    if etiquetas:
        libros = libros.filter(etiquetas__id__in=etiquetas).distinct()

    if orden == "asc":
        libros = libros.order_by("titulo")
    else:
        libros = libros.order_by("-titulo")

    todas_etiquetas = Etiqueta.objects.all()

    return render(request, "html/consulta_libros.html", {
        "libros": libros,
        "todas_etiquetas": todas_etiquetas,
        "etiquetas_seleccionadas": etiquetas,
        "orden": orden
    })

def listarEtiquetas(request):
    
    etiquetas = Etiqueta.objects.all()
    
    return render(request, 'html/listar_etiquetas.html', {
        'etiquetas': etiquetas
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

        messages.success(request, f"Se creó correctamente la etiqueta {etiqueta_nueva.nombre}")
        return redirect('lista_etiquetas')

    return render(request, 'html/crear_etiqueta.html', {'etiquetas': etiquetas})
