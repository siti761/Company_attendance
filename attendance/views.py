from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AttendanceForm
from .models import Attendance

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.user = request.user
            attendance.save()
            return redirect('attendance_success')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form': form})

def attendance_success(request):
    return render(request, 'attendance/attendance_success.html')
