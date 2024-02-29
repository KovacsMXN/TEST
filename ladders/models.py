from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta, timezone
from django.utils import timezone
#LADDERS BRANDS
class LattersBrands(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	imagen = models.ImageField(upload_to='ladders/brands/banners/', null=True)
	def __str__(self):
		return self.name

#LADDERS MATERIALS
class LattersMaterials(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	def __str__(self):
		return self.name

#LADDERS STATUS
class LattersStatus(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	def __str__(self):
		return self.name

#LADDERS DB MODEL
class Ladders(models.Model):
	id = models.AutoField(primary_key=True)
	imagen = models.ImageField(upload_to='ladders/images/')
	clave = models.CharField(max_length=255)
	brand = models.ForeignKey(LattersBrands, on_delete=models.CASCADE)
	modelo =  models.CharField(max_length=255)
	agregado = models.DateTimeField(default=timezone.now)
	material = models.ForeignKey(LattersMaterials, on_delete=models.CASCADE)
	pasos = models.IntegerField()
	status = models.ForeignKey(LattersStatus, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.clave) +  str(" / ") + str(self.brand) +  str(" / ") + str(self.modelo)

class LadderInspectionEntry(models.Model):
	id = models.AutoField(primary_key=True)
	ladder = models.ForeignKey(Ladders, on_delete=models.CASCADE)
	fecha = models.DateTimeField(default=timezone.now)
	usuario = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="1")
	@staticmethod
	def ha_sido_inspeccionado_este_mes(objeto_id):
		inicio_mes = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        # Corrección aquí: Uso correcto de timedelta para calcular el fin del mes
		fin_mes = inicio_mes + timedelta(days=31)  # Añade 31 días al inicio del mes
		fin_mes = fin_mes.replace(day=1) - timedelta(seconds=1)  # Retrocede al último momento del mes anterior
		return LadderInspectionEntry.objects.filter(ladder_id=objeto_id, fecha__range=(inicio_mes, fin_mes)).exists()
	def ha_sido_inspeccionado_el_mes_anterior(objeto_id):
		hoy = timezone.now()
        # Primer día del mes actual
		primer_dia_mes_actual = hoy.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        # Último día del mes anterior (un segundo antes del primer día del mes actual)
		fin_mes_anterior = primer_dia_mes_actual - timedelta(seconds=1)
        # Primer día del mes anterior
		inicio_mes_anterior = fin_mes_anterior.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

		return LadderInspectionEntry.objects.filter(
            ladder_id=objeto_id, 
            fecha__range=(inicio_mes_anterior, fin_mes_anterior)
        ).exists()
	def ha_sido_inspeccionado_dos_meses_atras(objeto_id):
		hoy = timezone.now()
        # Primer día del mes actual
		primer_dia_mes_actual = hoy.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        # Último día del mes anterior al anterior (un segundo antes del primer día del mes anterior)
		fin_mes_anterior_al_anterior = primer_dia_mes_actual.replace(day=1) - timedelta(days=1)
		fin_mes_anterior_al_anterior = fin_mes_anterior_al_anterior.replace(day=1) - timedelta(seconds=1)
        # Primer día del mes anterior al anterior
		inicio_mes_anterior_al_anterior = fin_mes_anterior_al_anterior.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

		return LadderInspectionEntry.objects.filter(
            ladder_id=objeto_id, 
            fecha__range=(inicio_mes_anterior_al_anterior, fin_mes_anterior_al_anterior)
        ).exists()