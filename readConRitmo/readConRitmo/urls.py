from readConRitmo import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

from readConRitmo import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('registro/', views.registro, name='register'),
    path('inicioSesion/', views.inicioSesion, name='inicioSesion'),
    path('inicioUsuario/', login_required(views.inicioUsuario, login_url='inicioSesion'), name='inicioUsuario'),
    path('cierreSesion/', login_required(views.signOut, login_url='inicioSesion'), name='cierreSesion'),
    path('libroDetalle/<int:pk>', login_required(views.libroDetalle, login_url='inicioSesion'), name='libroDetalle'),
    path('titulos/', login_required(views.titulos, login_url='inicioSesion'), name='titulos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)