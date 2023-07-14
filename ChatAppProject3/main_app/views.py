from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib.auth.models import User
from django.db import models
# Define the home view
# class CatCreate(LoginRequiredMixin, CreateView):
def home(request):
    return render(request, 'home.html')
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'profile_picture', 'password1', 'password2')
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            if 'profile_picture' in request.FILES:
                user.profile_picture = request.FILES['profile_picture']
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # Create a profile instance if it doesn't exist
        profile = Profile.objects.create(user=request.user)
    context = {
        'profile': profile,
        'user': request.user,
    }
    return render(request, 'profile.html', context)
