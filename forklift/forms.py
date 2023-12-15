import random
from django import forms

from django.contrib.auth.models import User

from .models import Forklifts
from .models import ForkliftServiceProviders
from .models import ForkliftBrands
from .models import ForkliftStatus
from .models import ForkliftOwners
from .models import InitialLoto

from .models import WaterEntry

from .models import ForkliftInspection

#DEF COLOR GEN FUNCTION
def color():
    color = "%03x" % random.randint(0, 0xFFF)
    return color

#DEF TAG PLACEHOLDER NUMBER FUNCTION
def tag():
    tag = random.randint(0, 0xFFF)
    return tag

class WaterTrackForm(forms.ModelForm):
    class Meta:
        model = WaterEntry
        fields = ['usuario','forklift']
        widgets={
            "forklift":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "usuario":forms.Select(attrs={'class':'form-control form-control-sm'}),
        }
    def __init__(self, *args, **kwargs):
        forklift_predefined1 = kwargs.pop('forklift', None)
        forklift_predefined2 = kwargs.pop('usuario', None)
        super(WaterTrackForm, self).__init__(*args, **kwargs)
        if forklift_predefined1:
            self.fields['forklift'].initial = forklift_predefined1
            self.fields['forklift'].disabled = True  # Hace el campo deshabilitado
            self.fields['usuario'].initial = forklift_predefined2
            self.fields['usuario'].disabled = True  # Hace el campo deshabilitado

class ForkliftForm(forms.ModelForm):
    class Meta:
        model = Forklifts
        fields = ['service_provider', 'clave', 'brand', 'powered' ,'modelo', 'serial', 'owner', 'imagen']
        widgets={
            "clave":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "modelo":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "serial":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "powered":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "service_provider" : forms.SelectMultiple(attrs={'class':'form-control','width':'100%'}),
            "brand":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "owner":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "model":forms.TextInput(attrs={'placeholder':'email@example.com','class':'form-control'}),
        }
    

class CreateForkliftForm(forms.ModelForm):
    class Meta:
        model = Forklifts
        fields = ['service_provider', 'clave', 'brand', 'modelo', 'serial', 'owner','imagen','powered']
        widgets={
            "clave":forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':tag}),
            "modelo":forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Example: XHLMI-TDT'}),
            "serial":forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'XHLMI-TDT-1998'}),
            "service_provider" : forms.SelectMultiple(attrs={'class':'form-control','width':'100%'}),
            "powered" :forms.Select(attrs={'class':'form-control form-control-sm'}),
            "brand":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "owner":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "model":forms.TextInput(attrs={'placeholder':'email@example.com','class':'form-control'}),
        }

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

class CreateServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ForkliftServiceProviders
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

class CreateForkliftBrands(forms.ModelForm):
    class Meta:
        model = ForkliftBrands
        fields = '__all__'
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "color":forms.TextInput(attrs={'class':'form-control', 'data-jscolor="{}"': '', 'value': color }),
        }

class CreateForkliftStatus(forms.ModelForm):
    class Meta:
        model = ForkliftStatus
        fields = '__all__'
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Name of the new forklift status'}),
            "color":forms.TextInput(attrs={'class':'form-control form-control-sm', 'data-jscolor="{}"': '', 'value': color}),
        }
        
class CreateForkliftLOTO(forms.ModelForm):
    class Meta:
        model = InitialLoto
        fields = ['reason','description']
        widgets={
            "reason":forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Maximum: 100 characters'}),
            "description":forms.Textarea(attrs={'rows':'5','class':'form-control form-control-sm','placeholder':'Additional information required'}),
        }

class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'width':'100%','class': 'form-control form-control-sm','placeholder':'Search reason'})
    )
    q_clave = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'width':'100%','class': 'form-control form-control-sm','placeholder':'FKL-0000'})
    )
    formstartusuario = forms.ModelChoiceField(queryset=User.objects.all().filter(is_staff=1),required=False,widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    formendusuario = forms.ModelChoiceField(queryset=User.objects.all().filter(is_staff=1),required=False,widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    sdate_min = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'datetime-local','class': 'form-control form-control-sm'}))
    sdate_max = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'datetime-local','class': 'form-control form-control-sm'}))
    edate_min = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'datetime-local','class': 'form-control form-control-sm'}))
    edate_max = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'datetime-local','class': 'form-control form-control-sm'}))

class EsInspectionForm(forms.ModelForm):
    class Meta:
        model = ForkliftInspection
        fields = ['forklift','check1','check2','check3','check4','check5','check6','check7','check8','check9','check10','check11','check12','des1','des2','des3','des4','des5','des6','des7','des8','des9','des10','des11','des12']
        widgets={
            "forklift":forms.Select(attrs={'class':'form-control form-control-sm'}),
            "check1":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "check2":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "check3":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "check4":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "check5":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "check6":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "check7":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "check8":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "check9":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "check10":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "check11":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "check12":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "des1": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
            "des2": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
            "des3": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
            "des4": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
            "des5": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
            "des6": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
            "des7": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
            "des8": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
            "des9": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
            "des10": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
            "des11": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
            "des12": forms.Textarea(attrs={'rows':'4','class':'form-control form-control-sm','placeholder':'Observaciones e informacion adicional'}),
        }