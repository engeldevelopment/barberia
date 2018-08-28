from django import forms
from .models import Servicio


class RegistrarServicio(forms.ModelForm):

	class Meta:
		model = Servicio
		fields = ['descripcion', 'precio']
		labels = {
			'descripcion': 'Descripción',
			'precio': 'Precio',
		}