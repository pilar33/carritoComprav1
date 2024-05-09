from django.shortcuts import render, redirect

from django.contrib.auth import logout
# Create your views here.

def home(request):
    return render(request,'home.html')

def loguin(request):
    return render(request, 'login.html')

def exit(request):
    logout(request)
    return redirect('Home')
