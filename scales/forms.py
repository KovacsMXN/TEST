import random
from django import forms

from django.contrib.auth.models import User

#IMPORT MODELS 
from .models import Scales, ScalesBrands, ScalesStatus, ScalesServiceProviders

#DEF COLOR GEN FUNCTION
def color():
    color = "%03x" % random.randint(0, 0xFFF)
    return color

#DEF TAG PLACEHOLDER NUMBER FUNCTION
def tag():
    tag = random.randint(0, 0xFFF)
    return tag


class CreateScaleForm(forms.ModelForm):
    class Meta:
        model = Scales
        fields = ['clave', 'brand', 'service_provider', 'modelo', 'serial', 'nmax','pesomax', 'clase', 'powersupply', 'imagen', 'status']
        widgets={
            "clave":forms.TextInput(attrs={'placeholder':'SCL-XXXX'}),
            "brand":forms.Select(),
            "serial":forms.TextInput(attrs={'placeholder':'Serial number'}),
            "modelo":forms.TextInput(attrs={'placeholder':'Model'}),
            "clase":forms.TextInput(attrs={'placeholder':'lll'}),
            "nmax":forms.TextInput(attrs={'placeholder':'10000'}),
            "pesomax":forms.TextInput(attrs={'placeholder':'Example: 10LB X 0.002LBS'}),
            "powersupply":forms.TextInput(attrs={'placeholder':'115 VAC 50/60Hz 1.0AMPS'}),
        }
        labels = {
            "clave": "Identification tag",
            "modelo": "Model",
            "powersupply": "Input",
            "clase": "Class",
            "pesomax": "Maximum Weight Capacity",
        }

class CreateScaleBrands(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateScaleBrands, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'no-asterisk'
    class Meta:
        model = ScalesBrands
        fields = '__all__'
        widgets={
            "name":forms.TextInput(attrs={'placeholder':'Example: Torrey S.A de C.V.'}),
            "color":forms.TextInput(attrs={'class':'form-control', 'data-jscolor="{}"': '', 'value': color }),
        }
        labels = {
            "name": "Brand name",
            "color": "Color",
            "imagen": "Imagen",
        }

class CreateScaleStatus(forms.ModelForm):
    class Meta:
        model = ScalesStatus
        fields = '__all__'
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Name of the scales status'}),
            "color":forms.TextInput(attrs={'class':'form-control form-control-sm', 'data-jscolor="{}"': '', 'value': color}),
        }
        labels = {
            "name": "Name of the status",
            "color": "Color",
        }

class CreateScaleServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ScalesServiceProviders
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
        labels = {
            "name": "Company's name:",
            "color": "Color",
            "imagen": "Banner",
        }