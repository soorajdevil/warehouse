from django import forms
from .models5 import Job

class JobScheduling(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['Time', 'ResourceNeeded', 'Permanent_Employee', 'Temporary_Employe']
       
        widgets = {
            'Time': forms.TextInput(attrs={'class': 'form-control'}),
            'ResourceNeeded': forms.TextInput(attrs={'class': 'form-control'}),
            'Permanent_Employee': forms.TextInput(attrs={'class': 'form-control'}),
            'Temporary_Employe': forms.TextInput(attrs={'class': 'form-control'}),
        }
