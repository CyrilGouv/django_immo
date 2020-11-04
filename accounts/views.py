from django.shortcuts import render, redirect
from django.contrib import messages

def register(request) :

    # Register User
    if request.method == 'POST' :
        messages.error(request, 'Testing Error Message')
        return redirect('register')
    
    else :
        return render(request, 'accounts/register.html')


def login(request) :

    # Login User
    if request.method == 'POST' :
        return
    
    else :
        return render(request, 'accounts/login.html')


def logout(request) :
    return redirect('index')


def dashboard(request) :
    return render(request, 'accounts/dashboard.html')
