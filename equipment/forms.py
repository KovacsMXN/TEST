from django import forms
from .models import Equipment_brands

class EquipmentBrandsForm(forms.ModelForm):
    class Meta:
        model = Equipment_brands
        fields = ['name']
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Manufacturer'}),
        }