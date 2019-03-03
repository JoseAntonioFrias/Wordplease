from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.core.validators import validate_email


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Contraseña')


class SignupForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Email',
            'password': 'Contraseña'}

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
        }

    def clean_username(self):
        """
        Normalizamos el dato del username y comprobamos que el username no existe ya en la BBDD
        Devolvemos el dato que validamos confirmado y validado de que no existe previamente
        """

        # obtenemos el username del formulario
        username = self.cleaned_data.get('username', '').lower()

        # comprobamos si existe el usuario en la tabla
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario {0} existe ya.'.format(username))
        return username

    def clean_email(self):
        """
        Comprobamos que el email no existe en la BBDD y que tiene el formato correcto.
        Devolvemos el dato que validamos confirmado y validado de que no existe previamente
        """

        # obtenemos el email del formulario
        email = self.cleaned_data.get('email', '').lower()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email {0} existe ya.'.format(email))
        elif validate_email(email):
            raise forms.ValidationError('El email {0} no tiene un formato válido.'.format(email))
        return email
