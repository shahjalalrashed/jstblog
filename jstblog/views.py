from django.shortcuts import render
import requests
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import RegistrationsForm,LoginForm
from django.contrib import messages
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User

# Create your views here.

def jstblogsite(request):
    return render(request,"index.html")

def jstcategory(request):
    return render(request,"category.html")

def jstcontact(request):
    return render(request,"contact.html")

def jstsingle(request):
    return render(request,"single.html")

def jstsignup(request):
    if request.user.is_authenticated:
        return redirect('bloghome')
    
    if request.method == 'POST':
        form=RegistrationsForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request,"Registrations successfull")   
            return redirect('bloglogin')            
    else:
        form=RegistrationsForm()
            
    context={
        'form':form,
    }
    return render(request,"signup.html",context)

def jstlogin(request):    
    if request.user.is_authenticated:
        return redirect('bloghome')
    else:
        if request.method == 'POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('bloghome')
            else:
                messages.info(request,"Enter correct username and password")
                return redirect('bloglogin')
        else:  
            return render(request, "login.html")
        
def jstlogout(request):   
    auth_logout(request)
    return redirect('bloglogin')

def jsteditprof(request):
    return render(request,"editprofile.html")

def jstchangepass(request):
    return render(request,"changepassword.html")
