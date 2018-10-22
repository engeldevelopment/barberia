from django import forms 
from .models import Contacto, Barbero


class RegistrarContacto(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = ['numero']
		labels = {'numero': 'Núemro',}


class BarberoForm(forms.ModelForm):
	class Meta:
		model = Barbero
		fields = ['cedula', 'nombre', 'apellido', 'apodo', 'activo']
		labels = {
			'cedula': 'Cédula', 
			'nombre': 'Nombre', 
			'apellido': 'Apellido', 
			'apodo': 'Apodo', 
			'activo': '¿Está trabajando?',
		} 		