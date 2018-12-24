
from django.db import models


class Servicio(models.Model):
	descripcion = models.CharField(max_length=30, unique=True)
	precio = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return "{desc}".format(desc=self.descripcion)


DIAS_LABORABLES = (
	('LUN', 'Lunes'),
	('MAR', 'Martes'),
	('MIE', 'Miércoles'),
	('JUE', 'Jueves'),
	('VIE', 'Viernes'),
	('SAB', 'Sábado'),
	('DOM', 'Domingo'),
)


class Horario(models.Model):
	dia = models.CharField(max_length=10,\
		choices=DIAS_LABORABLES, unique=True)
	hora_inicio = models.TimeField()
	hora_fin = models.TimeField()
	es_laborable = models.BooleanField(default = True)

	def __str__(self):
		return "{dia} de {inicio} a {fin}".format(dia=self.definir_dia(),\
			inicio=self.hora_inicio, fin=self.hora_fin)


	def definir_dia(self):
		nombre_dia = None
		if self.dia == "LUN":
			nombre_dia = "Lunes"
		elif self.dia == "MAR":
			nombre_dia = "Martes"
		elif self.dia == "MIE":
			nombre_dia = "Miércoles"
		elif self.dia == "JUE":
			nombre_dia = "Jueves"
		elif self.dia == "VIE":
			nombre_dia = "Viernes"
		elif self.dia == "SAB":
			nombre_dia = "Sábado"
		else:
			nombre_dia = "Domingo"					 
			
		return nombre_dia


class Corte(models.Model):
	nombre = models.CharField(max_length=40)
	imagen = models.ImageField(upload_to='cortes')

	def __str__(self):
		return self.nombre			