from django.db import models

class Job(models.Model):  
    Time=models.CharField(max_length=100)
    ResourceNeeded=models.IntegerField(null=True)
    Permanent_Employee=models.IntegerField(null= True)
    Temporary_Employe=models.IntegerField(null=True)