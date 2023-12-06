from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#FORKLIFT PROPERY
class ForkliftOwners(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=25)
	service_description = models.TextField()
	contact_person = models.CharField(max_length=100)
	address = models.TextField()
	website = models.URLField(blank=True, null=True)
	email = models.EmailField()
	imagen = models.ImageField(upload_to='forklifts/holders/banners/', null=True)
	def __str__(self):
		return self.name


#FORKLIFT SERVICE PROVIDERS
class ForkliftServiceProviders(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=25)
	service_description = models.TextField()
	contact_person = models.CharField(max_length=100)
	address = models.TextField()
	website = models.URLField(blank=True, null=True)
	email = models.EmailField()
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
	imagen = models.ImageField(upload_to='forklifts/equipment/')
	service_provider =  models.ManyToManyField(ForkliftServiceProviders, blank=True, null=True)
	clave = models.CharField(max_length=255)
	brand = models.ForeignKey(ForkliftBrands, on_delete=models.CASCADE)
	status = models.ForeignKey(ForkliftStatus,on_delete=models.PROTECT, default=1)
	modelo =  models.CharField(max_length=255)
	serial =  models.CharField(max_length=255)
	owner = models.ForeignKey(ForkliftOwners, on_delete=models.CASCADE)
	powered_opt = [
        ("G", "LPG"),
        ("E", "Electric"),
    ]
	powered = models.CharField(max_length=1, choices=powered_opt)
	def __str__(self):
		return str(self.clave) +  str(" / ") + self.brand.name + str(" / ") + self.modelo + str(" / ") + self.serial


#FORKLIFT LOTO
class InitialLoto(models.Model):
	id = models.AutoField(primary_key=True)
	forklift = models.ForeignKey(Forklifts, on_delete=models.CASCADE)
	start = models.DateTimeField(default=timezone.now)
	reason = models.CharField(max_length=100)
	description = models.TextField()
	startusuario = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="1")


#FORKLIFT LOTO
class Loto(models.Model):
	id = models.AutoField(primary_key=True)
	forklift = models.ForeignKey(Forklifts, on_delete=models.CASCADE)
	start = models.DateTimeField(default=timezone.now)
	end = models.DateTimeField(default=timezone.now)
	reason = models.CharField(max_length=100)
	description = models.TextField()
	startusuario = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="1")
	endusuario = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="1", related_name='end_lotos')