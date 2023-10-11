from django import forms
import re  
from . models1 import Supervise, Signin_Supervisor,ChatMessage
from django.core.exceptions import ValidationError




class supervisor(forms.ModelForm):
    class Meta:
        model = Supervise
        fields = ['supervisor_id', 'name', 'DOB', 'gender', 'contact_no', 'email', 'password']
        widgets = {
            'supervisor_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB': forms.DateInput(attrs={'class': 'form-control dob-input', 'type': 'date'}),  # Added a custom class
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control email-input'}),  # Added a custom class
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),  # Added a custom class
            'gender': forms.Select(attrs={'class': 'form-control supervisor-gender-select'}), # Added a custom class
        }

    GENDER_CHOICES = (
        ('Select', 'Select'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control supervisor-gender-select'})) # Added a custom class

    def clean_password(self):
        # Password validation rules (customize as needed)
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
             raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in password):
             raise ValidationError("Password must contain at least one letter.")
        return password
    
    def clean_contact_no(self):
        contact = str(self.cleaned_data.get('contact_no'))
        if not re.match(r'^\d{10}$', contact):
            raise ValidationError("Invalid contact number. Please enter a 10-digit phone number.")
        return contact
    
class LoginForm(forms.ModelForm):
    class Meta:
        model=Signin_Supervisor
        fields=['email','password']

        Widgets={
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            

        }



class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['text']