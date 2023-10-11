# Create your models here.
from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100)
    employee_id= models.AutoField(primary_key = True)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    contact_no=models.IntegerField(null=True)
    employee_type=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    UserType=models.CharField(max_length=100,default='Employee')
    
 
 
   






