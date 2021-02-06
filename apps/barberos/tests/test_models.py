from django.test import TestCase

from ..factories import BarberosFactory


class BarberoTest(TestCase):

	def test_cuando_este_activo_y_cambie_el_status_pasara_a_inactivo(self):

		self.barbero = BarberosFactory(inactivo=False)
		self.barbero.cambiar_status()

		self.assertFalse(self.barbero.activo)

	def test_cuando_este_inactivo_y_cambie_el_status_pasara_a_activo(self):

		self.barbero = BarberosFactory(inactivo=True)
		self.barbero.cambiar_status()

		self.assertTrue(self.barbero.activo)