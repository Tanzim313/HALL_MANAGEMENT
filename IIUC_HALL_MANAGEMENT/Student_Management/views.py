from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    return render(request,'student_management/home.html')

def Student_Registration(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # ইউজার সেভ করো
            messages.success(request, 'Account created successfully')  # সফল হলে বার্তা দেখাও
            return redirect('login')  # লগইন পেজে রিডাইরেক্ট করো
        else:
            messages.error(request, 'Error creating account')  # ত্রুটি থাকলে বার্তা দেখাও
    else:
        form = UserCreationForm()  # নতুন ফর্ম তৈরি করো
        
    return render(request,'student_management/sm.html')

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password')

    
    
    return render(request,'student_management/login.html')


def student_profile(request):
    return render(request,'student_management/pm.html')



