from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['attendance_type']
