from django.urls import path

from . import views
from .views import UserCreate

urlpatterns = [
    path('', views.home, name='home'),
    path('chats/', views.chat_index, name='index'),
]