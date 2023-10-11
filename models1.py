from django.db import models

class Supervise(models.Model):
    supervisor_id=models.AutoField(primary_key = True)
    name=models.CharField(max_length=100)
    DOB=models.DateField(null=True)
    gender=models.CharField(max_length=100)
    contact_no=models.IntegerField(null=True)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    UserType=models.CharField(max_length=100,default='Supervisor')


class Signin_Supervisor(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    
class ChatMessage(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Signin_Admin(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)