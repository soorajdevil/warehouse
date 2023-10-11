from django.db import models

class Veh(models.Model):
    
    vehicle_Catagories=models.CharField(max_length=25)
    Vehicle_Number=models.CharField(max_length=20)
    Description=models.CharField(max_length=100)