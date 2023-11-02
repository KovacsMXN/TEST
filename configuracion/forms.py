#IMPORT DJANGO FORMS AND FUCNTIONS
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

#IMPORT MODELS
from .models import Storage_Locations
from .models import Equipment_Locations
from .models import Equipment_brands

#FORM FOR USER EDIT
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User  
        fields = ['username', 'email','first_name','last_name','email','is_active','is_staff','is_superuser']
        widgets={
                   "username":forms.TextInput(attrs={'id':'autoSizingInputGroup','class':'form-control'}),
                   "first_name":forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),
                   "last_name":forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}),
                   "email":forms.TextInput(attrs={'placeholder':'email@example.com','class':'form-control'}),
        }
#FORM TO CREATE NEW STORAGE LOCATION
class CreateNewStorageLocation(forms.ModelForm):
    class Meta:
        model = Storage_Locations  # Especifica el modelo en el que se basará el formulario
        fields = ['name']  # Puedes utilizar '__all__' para incluir todos los campos del modelo# Si deseas incluir solo algunos campos específicos, puedes hacerlo de esta manera:# fields = ['campo1', 'campo2', 'campo3']
        widgets={
                   "name":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
        }
#FORM TO CREATE NEW EQUIPMENT LOCATION
class CreateNewEquipmentLocation(forms.ModelForm):
    class Meta:
        model = Equipment_Locations # Especifica el modelo en el que se basará el formulario
        fields = ['name']  # Puedes utilizar '__all__' para incluir todos los campos del modelo# Si deseas incluir solo algunos campos específicos, puedes hacerlo de esta manera:# fields = ['campo1', 'campo2', 'campo3']
        widgets={
                   "name":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
        }
#FORM TO CREATE NEW EQUIPMENT BRANDS
class CreateNewEquipmentBrands(forms.ModelForm):
    class Meta:
        model = Equipment_brands# Especifica el modelo en el que se basará el formulario
        fields = ['name']  # Puedes utilizar '__all__' para incluir todos los campos del modelo# Si deseas incluir solo algunos campos específicos, puedes hacerlo de esta manera:# fields = ['campo1', 'campo2', 'campo3']
        widgets={
                   "name":forms.TextInput(attrs={'placeholder':'Manufacturer name','class':'form-control'}),
        }
#FORM TO EDIT STORAGE LOCATIONS
class EditStorageLocation(forms.ModelForm):
    class Meta:
        model = Storage_Locations  # Especifica el modelo en el que se basará el formulario
        fields = ['name']  # Puedes utilizar '__all__' para incluir todos los campos del modelo# Si deseas incluir solo algunos campos específicos, puedes hacerlo de esta manera:# fields = ['campo1', 'campo2', 'campo3']
        widgets={
                   "name":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
        }