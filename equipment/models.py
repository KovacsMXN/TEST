from django.db import models
from storage.models import Locations
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
	location = models.ForeignKey(Locations, on_delete=models.CASCADE)
	description = models.TextField()
	imagen = models.ImageField(upload_to='equipment/main/', null=True)
	def __str__(self):
		return self.name
