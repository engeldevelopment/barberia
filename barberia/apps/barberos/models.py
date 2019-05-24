from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Barbero(models.Model):
	cedula = models.CharField(max_length=10, unique=True)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	apodo = models.CharField(max_length=30)
	activo = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse('barberos:detalle', kwargs={'pk':self.pk})

	def __str__(self):
		return "{nombre} ({apodo})".format(nombre=self.usuario.first_name,\
			apodo=self.apodo)

	def cambiar_status(self):
		self.activo = not self.activo
		return self.activo


class Contacto(models.Model):
	numero = models.CharField(max_length=15)
	barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)

	def __str__(self):
		return "{numero} {barbero}".format(numero=self.numero, \
			barbero=self.barbero)


class Banco(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return "{banco}".format(banco=self.nombre)


TIPO_CUENTA = (
	('A','Ahorro'),
	('C','Corriente')
)

class Cuenta(models.Model):
	numero = models.CharField(max_length=22, unique=True)
	banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
	barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=1, choices=TIPO_CUENTA)

	def __str__(self):
		return "{numero} ({banco})".format(numero=self.numero, \
			banco=self.banco)
