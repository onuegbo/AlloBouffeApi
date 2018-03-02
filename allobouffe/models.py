from django.db import models
from django.contrib.auth.models import User

# Create your models here.





class Restaurant(models.Model):
    #image = models.ImageField(upload_to='restaurants/', blank=False)
    created = models.ForeignKey('auth.User', related_name='restaurant', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, unique=True)
    addresse = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True)
    telephone = models.IntegerField(default = 0)
    is_hidden = models.BooleanField(default=False)

    
    
    class Meta:
        db_table= 'restaurant'
        ordering = ['created']
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        return self.name

  



class Product(models.Model):
    restaurant= models.ForeignKey(Restaurant, blank=False, related_name='products',  on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='nourritures/',  blank=False)
    name = models.CharField(max_length=128)
    delivery_time = models.DateTimeField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   

    class Meta:
        db_table='product'
        
    

    
    def __str__(self):
         return self.name

    

    
    
