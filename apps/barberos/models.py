
from django.db import models
from django.urls import reverse


class Barbero(models.Model):
	cedula = models.CharField(max_length=10, unique=True)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	apodo = models.CharField(max_length=30)
	activo = models.BooleanField(default=True)


	def get_absolute_url(self):
		return reverse('barberos:detalle-barbero', kwargs={'pk':self.pk})


	def __str__(self):
		return "{nombre} ({apodo})".format(nombre=self.nombre,\
			apodo=self.apodo)


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

	def definir_tipo(self):
		nombre = None
		if self.tipo == "A":
			nombre = "Ahorro"
		else:
			nombre = "Corriente"

		return nombre		
