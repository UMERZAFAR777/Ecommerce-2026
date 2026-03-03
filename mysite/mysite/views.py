from django.http import HttpRequest,HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from slider.models import Slider

def index(request):
    slider = Slider.objects.all()
    data = {
        'slider':slider,
    }
    return render (request,'index.html',data)

def myaccount(request):



    return render (request,'registration/myaccount.html')



def login_as(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = None

        try:
            user_obj = User.objects.get(email = username)
            user = authenticate(request,username = user_obj.username,password = password)
        except User.DoesNotExist:
            user = authenticate(request,username = username,password = password)  

        if user is not None:
            login (request,user)
            messages.success(request,'Login Successfully........!')
            return redirect ('index')
        else:
            messages.error(request,'Incorrect mail/passwoord...!')
            return redirect ('myaccount')   

    return render (request,'registration/myaccount.html')


def logout_as(request):
    logout(request,)
    messages.success(request,'Logout Successfully........!')
    return redirect ('index')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if User.objects.filter(username = username).exists():
            messages.error(request,'Username is Already Taken........!')
            return redirect ('register')
        

        if User.objects.filter(email = email).exists():
            messages.error(request,'Email is Already Taken........!')
            return redirect ('register')
        

        if password != password1:
            messages.error(request,'Password Doesnt Matched........!')
            return redirect ('register')
        

        user = User.objects.create_user(username=username,email=email,password=password)
       
        messages.success(request,'Created Successfully.........!')
        return redirect ('login_as')


    return render (request,'registration/myaccount.html')











