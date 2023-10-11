from django import forms
from . models import User
import re  
# from django.contrib.auth.forms import PasswordInput
from django.core.exceptions import ValidationError


class employee(forms.ModelForm):
    
    GENDER_CHOICES = [
        ('select', 'Select'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    EMPLOYEE_TYPE_CHOICES = [
        ('', 'Select'),
        ('Permanent', 'Permanent'),
        ('Temporary', 'Temporary'),
    ]

    gender = forms.CharField(
        widget=forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'})
    )
    
    employee_type = forms.CharField(
        widget=forms.Select(choices=EMPLOYEE_TYPE_CHOICES, attrs={'class': 'form-control'})
    )



    class Meta:
        model = User
        fields = ['name', 'employee_id', 'address', 'gender', 'employee_type', 'contact_no', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'employee_type': forms.Select(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    def clean_password(self):
        # Password validation rules (customize as needed)
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        # if not any(char.isdigit() for char in password):
        #     raise ValidationError("Password must contain at least one digit.")
        # if not any(char.isalpha() for char in password):
        #     raise ValidationError("Password must contain at least one letter.")
        return password
    
    def clean_contact_no(self):
        contact = str(self.cleaned_data.get('contact_no'))
        if not re.match(r'^\d{10}$', contact):
            raise ValidationError("Invalid contact number. Please enter a 10-digit phone number.")
        return contact

class Attendence(forms.ModelForm):
    class Meta:
        model=User
        fields=['employee_id','name']
       
        Widgets={
            'employee_id':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
           
        }