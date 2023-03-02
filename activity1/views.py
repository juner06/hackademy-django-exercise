from django.shortcuts import render, redirect, HttpResponse
from .forms import EditUserForm, EditUserProfileForm, UserRegistrationForm
from .models import Profile
from django.contrib import messages
from django import forms
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate



def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')

    
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login') 

        
def registration_view(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

def home_view(request):
    return render(request, 'users/home.html')

@login_required
def profile_view(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profile.html', {'profiles': profiles})

@login_required
@transaction.atomic
def edit_view(request):
    if request.method == "POST":
        user_form = EditUserForm(request.POST, instance=request.user)
        user_profile_form = EditUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            messages.success(request, 'Your profile has been successfully updated!')
            return redirect("profilepage")
    else:
        user_form = EditUserForm(instance=request.user)
        user_profile_form = EditUserProfileForm(instance=request.user.profile)
    return render(request, "users/editProfile.html", {"u_form":user_form, "p_form": user_profile_form})

