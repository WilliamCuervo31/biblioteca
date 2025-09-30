from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

    
class Usuario(AbstractUser):
    username = models.CharField('Nombre de Usuario', unique = True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    nombres = models.CharField('Nombres', max_length=200, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    forget_password_token = models.CharField(max_length=100)
    isAdmin = models.BooleanField('Rol', default=False)
    


    USERNAME_FIELD = 'username'
    EMAIL_FIELD ='email'
    REQUIRED_FIELDS = ['email', 'nombres']

    def __str__(self):
        return f'{self.nombres} {self.apellidos}' 

    

