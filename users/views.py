from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import LoginForm, RegisterForm

def home(request):
    return render(request, 'base.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Assuming your form saves the user or performs some registration logic
            user = form.save()
            # Optionally, log the user in directly after registration
            login(request, user)
            # Redirect to a new URL:
            return redirect('home')  # Change 'home' to your desired redirect target
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})   
    
def user_login(request):  
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

    
