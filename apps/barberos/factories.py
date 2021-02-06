import factory
from factory.django import DjangoModelFactory

from django.contrib.auth.models import User

from .models import Barbero



class UsersFactory(DjangoModelFactory):
	class Meta:
		model = User

	is_staff = True
	is_active = True
	username = 'engel12'
	password = '1234'
	first_name = 'Engel'
	last_name = 'Dev'


class BarberosFactory(DjangoModelFactory):
	class Meta:
		model = Barbero

	cedula = '22387256'
	apodo = 'El varón'
	activo = True
	usuario = factory.SubFactory(UsersFactory)

	class Params:
		inactivo = factory.Trait(
			activo=False
		)

