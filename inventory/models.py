from django.db import models

#MODELS MOTORS
#MOTORS BRANDS
class MotorsBrands(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	imagen = models.ImageField(upload_to='inventory/motors/brands/', null=True)
	def __str__(self):
		return self.name

#MOTORS MODEL
class Motors(models.Model):
	#ID NUMBER
	id = models.AutoField(primary_key=True)
	#MOTOR MODEL
	modelo = models.CharField(max_length=255)
	#MOTOR BRAND
	brand = models.ForeignKey(MotorsBrands, on_delete=models.PROTECT)
	#MOTOR VOLTS
	volts = models.CharField(max_length=255)
	#MOTOR AMPS
	amps = models.CharField(max_length=255)
	#MOTOR HORSEPOWER
	horsepower = models.CharField(max_length=255)
	#MOTOR PHASE
	phase = models.CharField(max_length=255)
	#MOTOR HZ
	hz = models.CharField(max_length=255)
	#MOTOR MAX RPMS
	maxrpm = models.CharField(max_length=255)
	#MOTOR SERVICE FACTOR
	sf = models.CharField(max_length=255)
	#MOTOR FRAME SIZE
	framenumero = models.CharField(max_length=255)
	#ENCLOSURE TYPE
	enclosure = models.CharField(max_length=255)

	#MOTOR IMAGEN
	imagen = models.ImageField(upload_to='inventory/motors/', blank=True, null=True)

	#MOTOR IMAGEN PLATE
	nameplate = models.ImageField(upload_to='inventory/motors/nameplates/', blank=True, null=True)

	#SYSTEM
	stock = models.IntegerField()
	stock_target = models.IntegerField()
	def __str__(self):
		return self.modelo