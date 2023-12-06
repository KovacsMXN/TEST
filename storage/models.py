from django.db import models

class Locations(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = color = models.CharField(max_length=10)
	def __str__(self):
		return self.name

class Storage(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = color = models.CharField(max_length=10)
	def __str__(self):
		return self.name