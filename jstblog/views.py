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
from bs4 import BeautifulSoup

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





def movreq(request):
    url = "https://www.imdb.com/chart/moviemeter/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table',  {'class': 'chart full-width'})
    rows = table.find_all('tr')
    
    minatlst=[]
    for row in rows:
        movies = []
        image = row.find('img')
        if image:
            movies.append(image['src'])
            movies.append(image['alt'])            
            minatlst.append(movies)
    print(minatlst)        
    return render(request, "movies.html", {'movies': minatlst})


def cbreq(request):
    url = "https://www.cricbuzz.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    li = soup.find('li',  {'class': 'cb-view-all-ga cb-match-card cb-bg-white'})
    rows = li.find_all('a')
    print(rows)
    
    for row in rows:
        card = row.find('a')
        if card:
            
           
    return render(request, "crickbuzzcopy.html")
