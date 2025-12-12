from django.utils import timezone
from django.db import models

from readConRitmo import settings
from user.models import Usuario

class Autor(models.Model):
    alias = models.CharField('Alias', max_length=150)
    descripcion = models.CharField('Descripción', max_length=500)
    nacionalidad = models.CharField('Nacionalidad', max_length=50)

    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'autores'
        db_table = 'autor'
        ordering = ['id']

    def __str__(self):
        return f'{self.alias}' 
    
class Etiqueta(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    descripcion = models.CharField('Descripción', max_length=300)
    color = models.CharField('Color', max_length=7)
    activo = models.BooleanField('Activo', default=True)

    padre = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='hijos'
    )

    class Meta:
        verbose_name = 'etiqueta'
        verbose_name_plural = 'etiquetas'
        db_table = 'etiqueta'
        ordering = ['id']

    def __str__(self):
        return f'{self.nombre},{self.color}'


class Libros(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=300)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to='portadasLibros', null=True)
    etiquetas = models.ManyToManyField(Etiqueta, through='LibroEtiqueta')


    def __str__(self):
        return f'{self.titulo},{self.autor_id}'
    
class LibroEtiqueta(models.Model):
    libro_id = models.ForeignKey(Libros, on_delete=models.CASCADE, verbose_name="LibroId")
    etiqueta_id = models.ForeignKey(Etiqueta, on_delete=models.CASCADE, verbose_name="EtiquetaId")
    fecha_creacion = models.DateTimeField('FechaCreacion', default=timezone.now())
    activo = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'libro_etiqueta'
        verbose_name_plural = 'libro_etiqueta'
        db_table = 'libro_etiqueta'
        ordering = ['id']

    def __str__(self):
        return f'{self.libro_id},{self.etiqueta_id}'    

class Experiencias(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    descripcion = models.CharField('Descripcion', max_length=300)
    fecha_creacion = models.DateField('FechaCreacion', default=timezone.now())
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="UsuarioId")
    foto = models.ImageField(verbose_name="FotoExperiencias", null=True, upload_to='fotosExperiencias')

    class Meta:
        verbose_name = 'experiencia'
        verbose_name_plural = 'experiencias'
        db_table = 'experiencias'
        ordering = ['id']

    def __str__(self):
        return f'{self.titulo}, {self.usuario_id}'
    
class Prestamo(models.Model):
    libro_id = models.ForeignKey(Libros, on_delete=models.CASCADE, verbose_name="LibroId")
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="UsuarioId")
    fecha_inicio = models.DateField('FechaCreacion', default=timezone.now())
    fecha_fin = models.DateField('FechaCreacion', default=timezone.now())
    observacion = models.CharField('Descripcion', max_length=300)

    class Meta:
        verbose_name = 'prestamo'
        verbose_name_plural = 'prestamos'
        db_table = 'prestamo'
        ordering = ['id']

    def __str__(self):
        return f'{self.libro_id.titulo}, {self.usuario_id.nombres}'
