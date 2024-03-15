from django.db import models

#SCALES BRANDS
class ScalesBrands(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	imagen = models.ImageField(upload_to='scales/brands/banners/', null=True)
	def __str__(self):
		return self.name
#SCALES SERVICE PROVIDERS
class ScalesServiceProviders(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=25)
	service_description = models.TextField()
	contact_person = models.CharField(max_length=100)
	address = models.TextField()
	website = models.URLField(blank=True, null=True)
	email = models.EmailField()
	imagen = models.ImageField(upload_to='scales/serviceproviders/banners/', null=True)
	def __str__(self):
		return self.name
#SCALE STATUS
class ScalesStatus(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	def __str__(self):
		return self.name
#SCALES 
class Scales(models.Model):
	id = models.AutoField(primary_key=True)
	clave= models.CharField(max_length=255)
	brand = models.ForeignKey(ScalesBrands, on_delete=models.CASCADE)
	service_provider =  models.ManyToManyField(ScalesServiceProviders, blank=True, null=True)
	modelo = models.CharField(max_length=255)
	serial = models.CharField(max_length=255)
	nmax = models.CharField(max_length=255)
	pesomax = models.CharField(max_length=255)
	clase = models.CharField(max_length=255)
	powersupply = models.CharField(max_length=255)
	imagen = models.ImageField(upload_to='scales/equipment/', null=True)
	status= models.ForeignKey(ScalesStatus, on_delete=models.CASCADE)
	def __str__(self):
		return self.clave
