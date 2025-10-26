from readConRitmo import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

from readConRitmo import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('/consultaLibro', views.consulta_libros, name='consulta_libro'),
    path('/listarEtiquetas', views.listarEtiquetas, name='lista_etiquetas'),
    path('/crearEtiqueta', views.crearEtiqueta, name='crear_etiqueta')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)