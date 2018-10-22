from django import forms 
from .models import Contacto, Barbero


class ContactoForm(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = ['numero']
		labels = {'numero': 'Núemro',}


class BarberoForm(forms.ModelForm):
	class Meta:
		model = Barbero
		fields = ['cedula', 'nombre', 'apellido', 'apodo']
		labels = {
			'cedula': 'Cédula:',
			'nombre': 'Nombre:',
			'apellido': 'Apellido:',
			'Apodo': 'Apodo:'
		}		