from django.shortcuts import render

from .models import Chat
# Create your views here.

def home(request):
    return render(request, 'home.html')

# class login(request):
#     return render(request, 'login.html')