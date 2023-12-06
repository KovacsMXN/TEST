from django import forms
from .models import Locations, Storage
import random

def color():
    color = "%03x" % random.randint(0, 0xFFF)
    return color

class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['name','color']
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Name of the new storage unit'}),
            "color":forms.TextInput(attrs={'class':'form-control form-control-sm ','data-jscolor="{}"': '', 'value': color}),
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = ['name','color']
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Name of the new location'}),
            "color":forms.TextInput(attrs={'class':'form-control form-control-sm ','data-jscolor="{}"': '', 'value': color}),
        }