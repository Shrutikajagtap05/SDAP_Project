from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
    return render(request,'about.html')

# User Registration
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        age = request.POST['age']
        gender = request.POST['gender']
        contact = request.POST['contact']

        if password == confirm_password:
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password)
            )
            user.save()
            return redirect('/login/')
        else:
            return render(request, 'register_user.html', {'error': 'Passwords do not match'})

    return render(request, 'register_user.html')

from django.contrib.auth import authenticate, login

# Login Page
def login(request):
    if request.method == 'POST':
        role = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(username=email, password=password)

        if user is not None and user.profile.role == role:  # Check if role matches
            login(request, user)
            return redirect('/')  # Redirect to the home page or dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials or role mismatch'})
    
    return render(request, 'login.html')

# Doctor Registration
def register_doctor(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        specialization = request.POST['specialization']
        experience = request.POST['experience']
        contact = request.POST['contact']

        if password == confirm_password:
            doctor = User.objects.create(
                username=username,
                email=email,
                password=make_password(password)
            )
            # Assuming user profile is extended with specialization, experience, and contact fields
            doctor.profile.specialization = specialization
            doctor.profile.experience = experience
            doctor.profile.contact = contact
            doctor.profile.role = 'doctor'  # Distinguishing doctor type
            doctor.save()
            return redirect('/login/')
        else:
            return render(request, 'register_doctor.html', {'error': 'Passwords do not match'})

    return render(request, 'register_doctor.html')