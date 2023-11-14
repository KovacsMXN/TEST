from django import forms
from .models import Forklifts, ForkliftServiceProviders, ForkliftBrands, ForkliftStatus, ForkliftOwners

class ForkliftForm(forms.ModelForm):
    class Meta:
        model = Forklifts
        fields = ['service_provider', 'clave', 'brand', 'status', 'modelo', 'serial', 'owner']
        widgets={
            "clave":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "modelo":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "serial":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "service_provider" : forms.SelectMultiple(attrs={'class':'form-control','width':'100%'}),
            "brand":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "status":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "owner":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "model":forms.TextInput(attrs={'placeholder':'email@example.com','class':'form-control'}),
        }
class CreateForkliftForm(forms.ModelForm):
    class Meta:
        model = Forklifts
        fields = ['service_provider', 'clave', 'brand', 'status', 'modelo', 'serial', 'owner','imagen']
        widgets={
            "clave":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "modelo":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "serial":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "service_provider" : forms.SelectMultiple(attrs={'class':'form-control','width':'100%'}),
            "brand":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "status":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "owner":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "model":forms.TextInput(attrs={'placeholder':'email@example.com','class':'form-control'}),
        }
class UploadImgForm(forms.ModelForm):
    class Meta:
        model = Forklifts
        fields = ['imagen']

class CreateForkliftOwnersForm(forms.ModelForm):
    class Meta:
        model = ForkliftOwners
        fields = '__all__'
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "phone_number":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "contact_person":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "website":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "email":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "address":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "service_description":forms.Textarea(attrs={'rows':'8','class':'form-control form-control-sm'}),
        }