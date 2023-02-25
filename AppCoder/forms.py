from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class EntregableFormulario(forms.Form):

    nombre = forms.CharField()
    fechaEntrega= forms.DateField()
    entregado =forms.CheckboxInput()

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields= ["username","email","first_name","last_name","password1","password2"]   

class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields= ["email","first_name","last_name","password1","password2"]   

class AvatarFormulario(forms.Form):

    class Meta:
        model=Avatar
        fields= ['user','user']   