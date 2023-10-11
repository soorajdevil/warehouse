from django import forms
from . models3 import Racks


class Stock(forms.ModelForm):
    class Meta:
        model=Racks
        fields=['rack_name','nof_bins','width','height','length']
       
        widgets = {
            'rack_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nof_bins': forms.TextInput(attrs={'class': 'form-control'}),
            'width': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.TextInput(attrs={'class': 'form-control'}),
            'length': forms.TextInput(attrs={'class': 'form-control'}),
        }
