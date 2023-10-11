from django import forms
from .models6 import Veh

class Ww(forms.ModelForm):
    class Meta:
        model = Veh
        fields = ['vehicle_Catagories', 'Vehicle_Number', 'Description']
       
        widgets = {
            'vehicle_Catagories': forms.TextInput(attrs={'class': 'form-control'}),
            'Vehicle_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.TextInput(attrs={'class': 'form-control'}),
        }
