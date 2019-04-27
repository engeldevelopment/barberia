from django import forms
from .models import Servicio


class ServicioForm(forms.ModelForm):

	class Meta:
		model = Servicio
		fields = ['descripcion', 'precio']
		labels = {
			'descripcion': 'Descripción',
			'precio': 'Precio',
		}
		widgets = {
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
			'precio': forms.NumberInput(attrs={'class': 'form-control'}),	
		}

