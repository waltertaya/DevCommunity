from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def def register(request):
    form  = UserCreationForm()
    return render(request, 'register.html', {'form': form})
    
