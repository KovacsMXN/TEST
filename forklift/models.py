from django.db import models
from django.utils import timezone

#FORKLIFT PROPERY
class ForkliftOwners(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	imagen = models.ImageField(upload_to='forklifts/holders/banners/', null=True)
	def __str__(self):
		return self.name


#FORKLIFT SERVICE PROVIDERS
class ForkliftServiceProviders(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	imagen = models.ImageField(upload_to='forklifts/serviceproviders/banners/', null=True)
	def __str__(self):
		return self.name


#FORKLIFT BRANDS
class ForkliftBrands(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	imagen = models.ImageField(upload_to='forklifts/brands/banners/', null=True)
	def __str__(self):
		return self.name



#FORKLIFT STATUS
class ForkliftStatus(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	def __str__(self):
		return self.name


#FORKLIFT DB MODEL
class Forklifts(models.Model):
	id = models.AutoField(primary_key=True)
	imagen = models.ImageField(upload_to='forklifts/equipment/', null=True)
	service_provider =  models.ManyToManyField(ForkliftServiceProviders, blank=True, null=True)
	clave = models.CharField(max_length=255)
	brand = models.ForeignKey(ForkliftBrands, on_delete=models.CASCADE)
	status = models.ForeignKey(ForkliftStatus,on_delete=models.PROTECT)
	modelo =  models.CharField(max_length=255)
	serial =  models.CharField(max_length=255)
	owner = models.ForeignKey(ForkliftOwners, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.brand) +  str(" / ") + self.modelo +str(" / ") + self.serial
