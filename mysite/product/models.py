from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.

class Main_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey(Main_Category,on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.main_category.name +"--"+ self.name
    
class Sub_Category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category.main_category.name +"--"+ self.category.name + "--"+ self.name   



class Section(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    section = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=300)
    img = models.CharField(max_length=800)
    price = models.IntegerField()
    sale = models.IntegerField()
    discount = models.IntegerField()
    total_quantity = models.IntegerField()
    availability = models.IntegerField()
    information = RichTextField()
    description = RichTextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    


    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("productdetails", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)



class Product_Img(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    img = models.CharField(max_length=800)


class Product_Information(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    title = models.CharField(max_length=400)
    description = models.CharField(max_length=400)





