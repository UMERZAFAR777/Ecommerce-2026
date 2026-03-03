from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from adminpanel import views
urlpatterns = [
   
    # path('admin/',include('adminpanel.urls')),
    path('',views.admin,name='admin'),
    path('adminindex/',views.adminindex,name='adminindex'),
    path('logout_ad/',views.logout_ad,name='logout_ad'),
    path('adminregister/',views.adminregister,name='adminregister'),
    path('slider/',views.slider,name='slider'),
    path('editslider/<id>/',views.slideredit,name='slideredit'),
    path('addslider/',views.addslider,name='addslider'),
    path('deleteslider/<id>/',views.deleteslider,name='deleteslider'),
]

if settings.DEBUG:
    urlpatterns+=static(
        settings.MEDIA_URL,document_root = settings.MEDIA_ROOT
    )