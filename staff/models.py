from django.db import models
from django.contrib.auth.models import User

class UsersExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numeroempleado = models.CharField(max_length=100)
    language_opts = [("ES", "Español"),("EN", "English"),]
    language = models.CharField(max_length=2, choices=language_opts)