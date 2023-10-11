from django.db import models

class Manager(models.Model):
    
    Name=models.CharField(max_length=100)
    Mobile=models.IntegerField(null=True)
    Gender=models.CharField(max_length=100)
    Date_of_Birth=models.DateField(null=True)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    RePassword=models.CharField(max_length=100)
    UserType=models.CharField(max_length=100,default='Manager')
    
    

