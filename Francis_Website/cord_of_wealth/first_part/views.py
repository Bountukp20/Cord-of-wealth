from django.shortcuts import render
from .models import *
from .forms import *
from django.core.mail import send_mail
# from .forms import *
from django.utils.crypto import get_random_string
# from django.db.models import Q
# from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

def home(request):
    return render(request, 'first_part/index.html')

@login_required(login_url='login')
def store(request):
    return render(request, 'first_part/shop.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['confirm']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'first_part/registration/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                auth.login(request,user)
                return redirect('login')
        else:
            return render (request,'first_part/registration/signup.html', {'error':'Password does not match!'})
    else:
        return render(request, 'first_part/registration/signup.html')

            

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('store')
        else:
            return render (request,'first_part/registration/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'first_part/registration/login.html')