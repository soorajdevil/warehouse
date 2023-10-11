from django.db import models
from .models7 import Products
from .models3 import Building,Racks
from .models6 import Veh


class Box(models.Model): 
    Box_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True)
    rack_id = models.ForeignKey(Racks, on_delete=models.CASCADE, null=True, blank=True)
    vehicle_id = models.ForeignKey(Veh, on_delete=models.CASCADE, null=True, blank=True)
    Box_Name = models.CharField(max_length=200)
    Current_Date = models.DateField(null=True)
    vehicle_transit = models.CharField(max_length=200, null=True, blank=True)
    Action = models.CharField(max_length=200, null=True, blank=True)

    
    def __str__(self):
        return self.Box_Name  # Return the desired field for display
    

    


    
    
    
    
