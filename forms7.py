from django import forms
from . models7 import Products


class Prod(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['Catagories', 'Product_Name', 'Total_Quantity', 'Product_Details']  # Correct the field name 'Catagories' to 'Categories'

        widgets = {
            'Catagories': forms.TextInput(attrs={'class': 'form-control'}),
            'Product_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Total_Quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'Product_Details': forms.TextInput(attrs={'class': 'form-control'}),
        }
         