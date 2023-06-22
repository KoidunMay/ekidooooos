from django.db import models
from mptt.models import MPTTModel
from ckeditor.fields import RichTextField

# Create your models here.




class Setting(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=155)
    number_one = models.CharField(max_length=100)
    number_two = models.CharField(max_length=100)
    email = models.EmailField()
    facebook = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    schedule = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    menuObject = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="image/") 
    melting = models.BooleanField(default=False)
    prise = models.FloatField()

    def __str__(self):
        return self.name
    
class SliderProduct(models.Model):
    menuObject = models.ForeignKey(Menu, on_delete=models.CASCADE)

# кылышкерек
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    servers = models.CharField(max_length=100)
    prep_time = models.PositiveIntegerField(default=0)
    cooc_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    image = models.ImageField()
    post = models.ForeignKey(
        Product,
        related_name="recipe",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    

class Discount(models.Model):
    productObject = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.CharField(max_length=25)
   


class Cheks(models.Model):
    humanIp = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    nomer = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    isPay = models.BooleanField(default=False, null=True, blank=True)

class CheksDetail(models.Model):
    productObject = models.ForeignKey(Product, on_delete = models.CASCADE, null=True, blank=True)
    totalSum = models.FloatField(null=True, blank=True)
    productCount = models.FloatField(default=1.0, null=True, blank=True)
    cheksObject = models.ForeignKey(Cheks, on_delete=models.CASCADE, null=True, blank=True)

#кылышкерек
class Coment(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()
    post = models.ForeignKey(Product, related_name="comment", on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

class Stol(models.Model):
    nomer = models.CharField(max_length=20)

class Bron(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    haumany = models.CharField(max_length=15)
    dait = models.CharField(max_length=33)
    stolObject = models.ForeignKey(Stol, on_delete=models.CASCADE, blank=True, null=True)

