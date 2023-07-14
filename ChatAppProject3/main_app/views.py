from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Chat
from .models import User
# Create your views here.

def home(request):
    return render(request, 'home.html')

def chat_index(request):
    chats = Chat.objects.all()
    return render(request, 'chats/index.html', {
        'chats' : chats
    })
