from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Barbero


class BarberoTest(TestCase):

	def setUp(self):
		self.engel12 = User.objects.create_user(
				username="engel12", 
				password="1234"
			)

		self.barbero = Barbero.objects.create(
				cedula="22387256",
				apodo="El varón",
				usuario=self.engel12
			)


	def test_cuando_este_activo_y_cambie_el_status_pasara_a_inactivo(self):

		self.barbero.cambiar_status()

		self.assertFalse(self.barbero.activo)

	def test_cuando_este_inactivo_y_cambie_el_status_pasara_a_activo(self):

		self.barbero.activo = False
		self.barbero.cambiar_status()

		self.assertTrue(self.barbero.activo)