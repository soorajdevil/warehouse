from django import forms
from . models8 import AttendenceForm


class TakeAttendence(forms.ModelForm):
    class Meta:
        model = AttendenceForm
        fields = [ 'Attendence']

    # Define choices for the "Attendence" field
    ATTENDANCE_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]

    # Use ChoiceField for "Attendence" with the defined choices
    Attendence = forms.ChoiceField(
        choices=ATTENDANCE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),  # Add class for styling if needed
    )
         