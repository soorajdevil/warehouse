from django.db import models
from .models import User


class AttendenceForm(models.Model):  
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    attendance_status = models.CharField(max_length=200)
    current_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.employee} - {self.attendance_status}"
    