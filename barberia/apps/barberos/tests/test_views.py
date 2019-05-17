from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import Barbero


class BarberoViewTest(TestCase):

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

	def test_cambiar_status_de_usuario_logueado_activo_cambiara_a_inactivo(self):

		url =  reverse('barberos:cambiar_status', 
			kwargs={'pk': self.barbero.pk})

		self.client.login(
			username=self.engel12.username, 
			password="1234"
			)

		response = self.client.post(url)

		self.assertEqual(200, response.status_code)