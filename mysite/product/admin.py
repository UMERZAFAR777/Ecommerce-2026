from django.contrib import admin
from product.models import *
# Register your models here.


class Product_Imgs(admin.TabularInline):
    model = Product_Img

class Product_Informations(admin.TabularInline):
    model = Product_Information


class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Imgs,Product_Informations)     



admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Section)
admin.site.register(Product,Product_Admin)


