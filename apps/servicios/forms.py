from django import forms
from .models import Servicio


class ServicioForm(forms.ModelForm):

	class Meta:
		model = Servicio
		fields = ['descripcion', 'precio', 'foto']
		labels = {
			'descripcion': 'Descripción',
			'precio': 'Precio',
			'foto': "Elige una foto"
		}
		widgets = {
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
			'precio': forms.NumberInput(attrs={'class': 'form-control'}),
			'foto': forms.FileInput(
					attrs={
						'class': 'form-control',
						'accept': 'image/*'
					}
				)
		}

