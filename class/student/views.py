from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.template import Context
# Create your views here.
def index(request):
    return render(request,"index.html")

def user_logout(request):
    if request.method=="POST":
        logout(request)
        
        return redirect('/')
    return render(request,"logout.html")


@login_required(login_url='/')
def home_view(request):
    return render(request,'home.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is not None :
            form=login(request,user)
            messages.success(request,f'welcome{username}!!')
            # return render(request,'login.html')
            return redirect('/')
        else:
            messages.info(request,f'account does not exit plz sign in')
    
    form=AuthenticationForm()
    # return render(request,'login.html',{'form':form,'title':'login here'})
    return render(request,'login.html',{'form':form})

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created')
            # return redirect('index')
            return redirect('/login')
            # return render(request,'login.html')
    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form,'title':'register here'})


def courseAdd(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,f'Your account has been created')
            # return redirect('index')
            return redirect('/')
            # return render(request,'login.html')
    else:
        form=CourseForm()
    return render(request,'register.html',{'form':form,'title':'register here'})

def enrollStudent(request):
    if request.method=='POST':
        form=StudentRegisteredForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,f'Your account has been created')
            # return redirect('index')
            return redirect('/')
            # return render(request,'login.html')
    else:
        form=StudentRegisteredForm()
    return render(request,'register.html',{'form':form,'title':'register here'})

def addChapter(request):
    if request.method=='POST':
        form=ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,f'Your account has been created')
            # return redirect('index')
            return redirect('/')
            # return render(request,'login.html')
    else:
        form=ChapterForm()
    return render(request,'register.html',{'form':form,'title':'register here'})

def completedChapter(request):
    if request.method=='POST':
        form=CompletedForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,f'Your account has been created')
            # return redirect('index')
            return redirect('/')
            # return render(request,'login.html')
    else:
        form=CompletedForm()
    return render(request,'register.html',{'form':form,'title':'register here'})


