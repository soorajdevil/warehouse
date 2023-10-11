from django.db import models
from django.utils import timezone 

class Building(models.Model):  
    Building_Name=models.CharField(max_length=100)
    Area=models.CharField(max_length=100)
    Floor=models.CharField(max_length=100)
    Identifer=models.CharField(max_length=100)
    Structure=models.CharField(max_length=100)
    Height=models.IntegerField(null= True)
    Total_No_Racks=models.IntegerField(null= True)    
    
    def __str__(self):
        return self.Building_Name  # Return the desired field for display
    
class Racks(models.Model):  
    foreign_key_fied =models.ForeignKey(Building, on_delete=models.CASCADE,null=True,blank=True)
    rack_name = models.CharField(max_length = 30)
    #weight = models.IntegerField(null=True)
    nof_bins = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    length = models.IntegerField(null=True)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.rack_name  # Return the desired field for display
    
    