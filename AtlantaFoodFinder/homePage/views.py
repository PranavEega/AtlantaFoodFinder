from functools import cache

from django.shortcuts import render, redirect

from . forms import UserRegistrationForm, UserLoginForm

#Authetication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.

def home(request):
    return render(request, 'homePage/index.html')

def register(request):

    form = UserRegistrationForm()

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/my-login')

    context = {'registerform': form}

    return render(request, "homePage/register.html", context = context)

def my_login(request):

    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect('/search')

    context = {'loginform': form}

    return render(request, "homePage/my_login.html", context = context)


def user_logout(request):
    logout(request)
    return redirect('home')



