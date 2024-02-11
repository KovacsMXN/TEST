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
	last_batery = models.DateTimeField(default=timezone.now)
	batery_target= models.IntegerField()
	def __str__(self):
		return str(self.clave) +  str(" / ") + self.brand.name + str(" / ") + self.modelo + str(" / ") + self.serial


#FORKLIFT LOTO
class WaterEntry(models.Model):
	id = models.AutoField(primary_key=True)
	forklift = models.ForeignKey(Forklifts, on_delete=models.CASCADE)
	fecha = models.DateTimeField(default=timezone.now)
	usuario = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="1")


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

#FORKLIFT INSPECTION
class ForkliftInspection(models.Model):
	id = models.AutoField(primary_key=True)
	forklift = models.ForeignKey(Forklifts, on_delete=models.CASCADE)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	fecha = models.DateTimeField(default=timezone.now)
	check1 = models.BooleanField()
	check2 = models.BooleanField()
	check3 = models.BooleanField()
	check4 = models.BooleanField()
	check5 = models.BooleanField()
	check6 = models.BooleanField()
	check7 = models.BooleanField()
	check8 = models.BooleanField()
	check9 = models.BooleanField()
	check10 = models.BooleanField()
	check11 = models.BooleanField()
	check12 = models.BooleanField()
	des1 = models.TextField(null=True,blank=True)
	des2 = models.TextField(null=True,blank=True)
	des3 = models.TextField(null=True,blank=True)
	des4 = models.TextField(null=True,blank=True)
	des5 = models.TextField(null=True,blank=True)
	des6 = models.TextField(null=True,blank=True)
	des7 = models.TextField(null=True,blank=True)
	des8 = models.TextField(null=True,blank=True)
	des9 = models.TextField(null=True,blank=True)
	des10 = models.TextField(null=True,blank=True)
	des11 = models.TextField(null=True,blank=True)
	des12 = models.TextField(null=True,blank=True)
	valid = models.BooleanField()
