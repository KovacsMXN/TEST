import random
from django import forms

from django.contrib.auth.models import User

from .models import LattersStatus, LattersMaterials, LattersBrands, Ladders, LadderInspectionEntry

#DEF COLOR GEN FUNCTION
def color():
    color = "%03x" % random.randint(0, 0xFFF)
    return color

#DEF TAG PLACEHOLDER NUMBER FUNCTION
def tag():
    tag = random.randint(0, 0xFFF)
    return tag

class CreateLadderStatus(forms.ModelForm):
    class Meta:
        model = LattersStatus
        fields = '__all__'
        widgets={
            "name":forms.TextInput(attrs={'placeholder':'Name of the new ladder status'}),
            "color":forms.TextInput(attrs={'data-jscolor="{}"': '', 'value': color}),
        }
        labels = {
            "name": "Name of the status",
        }

class CreateLadderMaterials(forms.ModelForm):
    class Meta:
        model = LattersMaterials
        fields = '__all__'
        widgets={
            "name":forms.TextInput(attrs={'placeholder':'Name of the new ladder material'}),
            "color":forms.TextInput(attrs={'data-jscolor="{}"': '', 'value': color}),
        }
        labels = {
            "name": "Name of the material",
        }
class CreateLadderBrands(forms.ModelForm):
    class Meta:
        model = LattersBrands
        fields = '__all__'
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Name of the new ladder brand'}),
            "color":forms.TextInput(attrs={'class':'form-control', 'data-jscolor="{}"': '', 'value': color }),
        }
        labels = {
            "name": "Name of the brand",
        }
class CreateLadderForm(forms.ModelForm):
    class Meta:
        model = Ladders
        fields = ['clave', 'brand', 'modelo', 'material', 'pasos', 'status', 'imagen']
        widgets = {
            "clave": forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Clave'}),
            "brand": forms.Select(attrs={'class': 'form-control form-control-sm'}),
            "modelo": forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Model'}),
            "material": forms.Select(attrs={'class': 'form-control form-control-sm'}),
            "pasos": forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter # of steps'}),
            "status": forms.Select(attrs={'class': 'form-control form-control-sm'}),
        }
        labels = {
            "clave": "Identification tag",
            "modelo": "Model",
        }
class LadderInspectionForm(forms.ModelForm):
    class Meta:
        model = LadderInspectionEntry
        fields = ['usuario','ladder']
        widgets={
            "ladder":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "usuario":forms.Select(attrs={'class':'form-control form-control-sm'}),
        }
    def __init__(self, *args, **kwargs):
        ladder_predefined1 = kwargs.pop('ladder', None)
        ladder_predefined2 = kwargs.pop('usuario', None)
        super(LadderInspectionForm, self).__init__(*args, **kwargs)
        if ladder_predefined1:
            self.fields['ladder'].initial = ladder_predefined1
            self.fields['ladder'].disabled = True  # Hace el campo deshabilitado
            self.fields['usuario'].initial = ladder_predefined2
            self.fields['usuario'].disabled = True  # Hace el campo deshabilitado