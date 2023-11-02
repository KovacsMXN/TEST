#IMPORT DJANGO FORMS AND FUCNTIONS
from django import forms

#IMPORT EQUIPMENT MODEL
from configuracion.models import Equipment

class EditEquipment(forms.ModelForm):
    class Meta:
        model = Equipment  # Especifica el modelo en el que se basará el formulario
        fields = '__all__'  # Puedes utilizar '__all__' para incluir todos los campos del modelo# Si deseas incluir solo algunos campos específicos, puedes hacerlo de esta manera:# fields = ['campo1', 'campo2', 'campo3']
        widgets={
                   "name":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
                   "model":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
                   "serial":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
                   "fa_number":forms.NumberInput(attrs={'placeholder':'Name','class':'form-control'}),
                   "brand":forms.Select(attrs={'class':'form-control'}),
                   "location":forms.Select(attrs={'class':'form-control'}),
                   "description":forms.Textarea(attrs={'rows':'3','class':'form-control'}),
        }
class ImagenForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['imagen']