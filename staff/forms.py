from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import UsersExtension

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Reemplaza "CustomUser" con el nombre de tu modelo de usuario personalizado
        fields = ('username', 'password1', 'password2')
        widgets={
                   "username":forms.TextInput(attrs={'class':'form-control'}),
        }
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','is_active','is_staff','is_superuser')
        widgets={
                "username":forms.TextInput(attrs={'class':'form-control'}),
                "first_name":forms.TextInput(attrs={'class':'form-control'}),
                "last_name":forms.TextInput(attrs={'class':'form-control'}),
                "email":forms.TextInput(attrs={'class':'form-control'}),
                "is_active":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                "is_staff":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                "is_superuser":forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
class CustomUsersExtension(forms.ModelForm):
    class Meta:
        model = UsersExtension
        fields = ('numeroempleado','language')
        widgets={
                "numeroempleado":forms.TextInput(attrs={'class':'form-control'}),
                "language":forms.Select(attrs={'class':'form-control form-control'}),
        }
    def __init__(self, *args, **kwargs):
        forklift_predefined1 = kwargs.pop('numeroempleado', None)
        forklift_predefined2 = kwargs.pop('language', None)
        super(CustomUsersExtension, self).__init__(*args, **kwargs)
        if forklift_predefined1:
            self.fields['numeroempleado'].initial = forklift_predefined1
            self.fields['language'].initial = forklift_predefined2