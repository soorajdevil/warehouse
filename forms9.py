from django import forms
from .models9 import Box
from .models7 import Products
from .models6 import Veh
from .models3 import Building, Racks

class BoxForm(forms.ModelForm):
    product_id = forms.ModelChoiceField(
        queryset=Products.objects.all(),
        empty_label="Select product",
        to_field_name='Product_Name',
        widget=forms.Select(attrs={'class': 'form-select'})  # Use 'form-select' for Bootstrap 5
    )
    building_id = forms.ModelChoiceField(
        queryset=Building.objects.all(),
        empty_label="Select building",
        to_field_name='Building_Name',
        widget=forms.Select(attrs={'class': 'form-select'})  # Use 'form-select' for Bootstrap 5
    )
    rack_id = forms.ModelChoiceField(
        queryset=Racks.objects.all(),
        empty_label="Select rack",
        to_field_name='rack_name',
        widget=forms.Select(attrs={'class': 'form-select'})  # Use 'form-select' for Bootstrap 5
    )

    class Meta:
        model = Box
        fields = ['product_id', 'building_id', 'rack_id', 'Box_Name']

class BuildingSearchForm(forms.Form):
    building = forms.ModelChoiceField(
        queryset=Building.objects.all(),
        empty_label='Select a building',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    


class BoxTransit(forms.Form):
    box_select = forms.CharField()  # Add the appropriate field types
    vehicle_transit = forms.IntegerField()
    box_action = forms.CharField()