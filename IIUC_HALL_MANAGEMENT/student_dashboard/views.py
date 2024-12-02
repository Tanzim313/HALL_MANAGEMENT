from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


def dashboard(request):
    return render(request,'student_dashboard/dashboard.html')
def meal_login(request):
    return render(request,'student_dashboard/meal_login.html')

 
def meal_management(request):
    return render(request,'student_dashboard/meal_management.html')
