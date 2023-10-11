from django.db import models
from.models3 import Racks

class Products(models.Model):
    foreign_key_fied =models.ForeignKey(Racks, on_delete=models.CASCADE,null=True,blank=True)
    Catagories=models.CharField(max_length=100)
    Product_Name=models.CharField(max_length=50)
    Total_Quantity=models.IntegerField(null=True)
    Product_Details=models.CharField(max_length=100)

    def __str__(self):
        return self.Product_Name  # Return the desired field for display


    