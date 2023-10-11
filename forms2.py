from django import forms
from . models3 import Building


class Build(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['Building_Name', 'Area', 'Floor', 'Identifer', 'Structure', 'Height', 'Total_No_Racks']

        widgets = {
            'Building_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Area': forms.TextInput(attrs={'class': 'form-control'}),
            'Floor': forms.TextInput(attrs={'class': 'form-control'}),
            'Identifer': forms.TextInput(attrs={'class': 'form-control'}),
            'Structure': forms.TextInput(attrs={'class': 'form-control'}),
            'Height': forms.TextInput(attrs={'class': 'form-control'}),
            'Total_No_Racks': forms.TextInput(attrs={'class': 'form-control'}),
        }