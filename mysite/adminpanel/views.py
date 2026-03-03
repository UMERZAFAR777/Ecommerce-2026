from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from slider.models import Slider
# Create your views here.


def admin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request,username = username , password = password)

        if user and user.is_superuser:
            login(request,user)
            messages.success(request,'Admin Login Successfully.....!')
            return redirect ('adminindex')
        else:
            messages.error(request,'Incorrect username/password or You are not admin....!')
            return redirect ('admin')

    return render (request,'adminpanel/adminlogin.html')

def adminindex(request):
    return  render (request,'adminpanel/adminindex.html')



def logout_ad(request):
    logout(request,)
    messages.success(request,'Logged out Successfully.....!')
    return redirect ('admin')


def adminregister(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password != password1:
            messages.error(request,"Password Doesnt Matched........!")
            return redirect ('adminregister')
        
        if User.objects.filter(username = username).exists():
            messages.error(request,"Username is Already Taken........!")
            return redirect ('adminregister')
        
        user = User.objects.create_user(username= username , password = password)

        user.is_staff = True
        user.is_superuser = True
        user.save()
        messages.success(request,"Admin Registered Successfully........!")
        return redirect ('admin')



    return render (request,'adminpanel/adminregister.html')




def slider(request):
    slider = Slider.objects.all()
    data = {
        'slider':slider
    }
    return render (request,'adminpanel/slider/slider.html',data)





def slideredit(request, id):
    slider = Slider.objects.get(id=id)

    if request.method == "POST":
        slider.name = request.POST.get('name', slider.name)
        slider.img = request.POST.get('img', slider.img)
        slider.sale = request.POST.get('sale', slider.sale)
        slider.discount = request.POST.get('discount', slider.discount)
      
        slider.discount_deal = request.POST.get('discount_deal', slider.discount_deal)

        slider.save()
        messages.success(request, 'Edit Successfully!')
        return redirect('slider')

    data = {
        'slider': slider
    }
    return render(request, 'adminpanel/slider/slideredit.html', data)




def addslider(request):
  
    if request.method == "POST":
        name = request.POST.get('name')
        img  = request.FILES.get('img')
        sale = request.POST.get('sale')
        discount = request.POST.get('discount')
        discount_deal = request.POST.get('discount_deal')
        link = request.POST.get('link',"-")

        if not img:
            messages.error(request,"Upload Image......!")
            return  redirect ('addslider')
        
        slider = Slider.objects.create(name = name,img = img,sale = sale,discount = discount,discount_deal=discount_deal,link = link)

        slider.save()

        messages.success(request,'Add Slider Successfully....!')

        return redirect ('slider')




   
    
    return render(request, 'adminpanel/slider/addslider.html')



def deleteslider(request,id):
    slider = Slider.objects.get(id = id)
    slider.delete()

    messages.success(request,'Delete Slider Successfully....!')
    return redirect ('slider')

