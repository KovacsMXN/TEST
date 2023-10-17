from django.db import models
from django.utils import timezone

class SupluMX(models.Model):
	id = models.AutoField(primary_key=True)
	copy = models.BooleanField(default=True)

class Storage_Locations(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	add_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.name

class Equipment_Locations(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Equipment_brands(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Equipment(models.Model):
	fa_number = models.IntegerField()
	name = models.CharField(max_length=255)
	brand = models.ForeignKey(Equipment_brands, on_delete=models.CASCADE)
	model = models.CharField(max_length=255)
	serial = models.CharField(max_length=255)
	location = models.ForeignKey(Equipment_Locations, on_delete=models.CASCADE)
	description = models.TextField()
	def __str__(self):
		return self.name
