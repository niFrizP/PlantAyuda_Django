from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=200)
    stock = forms.IntegerField(min_value=1, max_value=600)
    class Meta:
        model = Producto
        fields = '__all__'

class CustomUserForm (UserCreationForm):
    pass

class CustomUserForm (UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
