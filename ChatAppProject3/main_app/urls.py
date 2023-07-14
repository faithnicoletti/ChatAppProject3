from django.urls import path

from . import views
from .views import UserCreate

urlpatterns = [
    path('', views.home, name='home'),
    path('user/create/', UserCreate.as_view(), name='user-create'),
    path('chats/', views.chat_index, name='index'),
]