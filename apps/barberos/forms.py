from django import forms 
from .models import Contacto


class ContactoForm(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = ['numero']
		labels = {'numero': 'Núemro',}