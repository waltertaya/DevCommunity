from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form  = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})
    

def login(request):
    return render(request, 'login/login.html')