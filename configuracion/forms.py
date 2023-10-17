from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import Storage_Locations
from .models import Equipment_Locations
from .models import Equipment_brands

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User  # Asegúrate de importar User desde django.contrib.auth.models
        fields = ['username', 'email','first_name','last_name','email','is_active','is_staff','is_superuser']
        widgets={
                   "username":forms.TextInput(attrs={'id':'autoSizingInputGroup','class':'form-control'}),
                   "first_name":forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),
                   "last_name":forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}),
                   "email":forms.TextInput(attrs={'placeholder':'email@example.com','class':'form-control'}),
        }
class CreateNewStorageLocation(forms.ModelForm):
    class Meta:
        model = Storage_Locations  # Especifica el modelo en el que se basará el formulario
        fields = ['name']  # Puedes utilizar '__all__' para incluir todos los campos del modelo# Si deseas incluir solo algunos campos específicos, puedes hacerlo de esta manera:# fields = ['campo1', 'campo2', 'campo3']
        widgets={
                   "name":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
        }
class CreateNewEquipmentLocation(forms.ModelForm):
    class Meta:
        model = Equipment_Locations # Especifica el modelo en el que se basará el formulario
        fields = ['name']  # Puedes utilizar '__all__' para incluir todos los campos del modelo# Si deseas incluir solo algunos campos específicos, puedes hacerlo de esta manera:# fields = ['campo1', 'campo2', 'campo3']
        widgets={
                   "name":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
        }
class CreateNewEquipmentBrands(forms.ModelForm):
    class Meta:
        model = Equipment_brands# Especifica el modelo en el que se basará el formulario
        fields = ['name']  # Puedes utilizar '__all__' para incluir todos los campos del modelo# Si deseas incluir solo algunos campos específicos, puedes hacerlo de esta manera:# fields = ['campo1', 'campo2', 'campo3']
        widgets={
                   "name":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
        }
class EditStorageLocation(forms.ModelForm):
    class Meta:
        model = Storage_Locations  # Especifica el modelo en el que se basará el formulario
        fields = ['name']  # Puedes utilizar '__all__' para incluir todos los campos del modelo# Si deseas incluir solo algunos campos específicos, puedes hacerlo de esta manera:# fields = ['campo1', 'campo2', 'campo3']
        widgets={
                   "name":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
        }