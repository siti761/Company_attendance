from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Attendance(models.Model):
    WORK_FROM_HOME = 'WFH'
    WORK_FROM_OFFICE = 'WFO'
    ATTENDANCE_CHOICES = [
        (WORK_FROM_HOME, 'Work from Home'),
        (WORK_FROM_OFFICE, 'Work from Office'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    date = models.DateField(auto_now_add=True)  # Automatically set to today's date
    attendance_type = models.CharField(
        max_length=3,
        choices=ATTENDANCE_CHOICES,
        default=WORK_FROM_OFFICE,
    )

    def __str__(self):
        return f"{self.user.username} - {self.attendance_type} on {self.date}"
