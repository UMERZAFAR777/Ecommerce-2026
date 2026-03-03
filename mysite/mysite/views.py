from django.http import HttpRequest,HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    return render (request,'index.html')


















