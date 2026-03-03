from django.db import models

# Create your models here.
class Slider (models.Model):

    DISCOUNT_DEAL = (
        ('HOT DEALS','HOT DEALS'),
        ('NEW ARRIVAL','NEW ARRIVAL')
    )



    name = models.CharField(max_length=100)
    img = models.FileField(upload_to='slider_img/',unique=True,default=None)
    discount_deal = models.CharField(choices=DISCOUNT_DEAL , max_length=300)
    discount = models.IntegerField()
    sale = models.IntegerField()
    link = models.CharField(max_length=300)



    def __str__(self):
        return self.name


