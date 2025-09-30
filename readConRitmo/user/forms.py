from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import Usuario

class CustomUserCreationForm(UserCreationForm):
    
    def clean(self):
        super().clean()

        nombres = self.cleaned_data.get('nombres')
        if nombres and nombres.strip():
            if any(c.isspace() for c in nombres):
                self.add_error('nombres', 'El nombre no puede contener espacios en blanco.')

            apellidos = self.cleaned_data.get('apellidos')
            if apellidos and apellidos.strip():
                if any(c.isspace() for c in apellidos):
                    self.add_error('apellidos', 'El apellido no puede contener espacios en blanco.')

            email = self.cleaned_data.get('email')
            if email and email.strip():
                if any(c.isspace() for c in email):
                    self.add_error('email', 'El correo electrónico no puede contener espacios en blanco.')

            username = self.cleaned_data.get('username')
            if username and username.strip(' '):
                if any(c.isspace() for c in username):
                    self.add_error('username', 'El nombre de usuario no puede contener espacios en blanco.')

            return self.cleaned_data
        
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombres', 'apellidos', 'isAdmin']
        
        
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        if password1 and any(c.isspace() for c in password1):
            self.add_error('password1', 'La contraseña no puede contener espacios en blanco.')

        return password1

        

