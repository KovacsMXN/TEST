from django.db import models
from django.utils import timezone

#FORKLIFT PROPERY
class ForkliftOwners(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	website = models.TextField()
	phone = models.CharField(max_length=255)
	adress = models.TextField()
	email = models.TextField()

#FORKLIFT SERVICE PROVIDERS
class ForkliftOwners(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	website = models.TextField()
	phone = models.CharField(max_length=255)
	adress = models.TextField()
	email = models.TextField()

#FORKLIFT BRANDS
class ForkliftBrands(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)

#FORKLIFT STATUS
class ForkliftStatus(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=255)

#FORKLIFT LOG
class ForkliftLog(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=255)

#FORKLIFT DB MODEL
class Forklifts(models.Model):
	id = models.AutoField(primary_key=True)
	brand = models.ForeignKey(ForkliftBrands, on_delete=models.CASCADE)
	modelo = models.TextField()
	serial = models.TextField()
	owner = models.ForeignKey(ForkliftOwners, on_delete=models.CASCADE)
	color = models.CharField()