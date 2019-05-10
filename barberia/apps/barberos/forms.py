from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from .models import Contacto, Barbero


class ContactoForm(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = ['numero']
		labels = {
			'numero': 'Número telefónico',
		}
		
		widgets = {
			'numero': forms.TextInput(attrs={'class': 'form-control'})
		}


class UserForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'password1',
			'password2'
		]


class BarberoForm(forms.ModelForm):

	class Meta:
		model = Barbero
		fields = ['cedula', 'apodo']
		labels = {
			'cedula': 'Cédula',
			'Apodo': 'Apodo'
		}
		widgets = {
			'cedula': forms.TextInput(attrs={'class': 'form-control'}),
			'apodo': forms.TextInput(attrs={'class': 'form-control'})	
		}