from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Categories(models.TextChoices):
    ELECTRONICS = 'electronics'
    LAPTOPS = 'Laptops'
    ARTS = 'Arts'
    FOOD = 'Food'
    HOME = 'Home'
    KITCHEN = 'Kitchen'


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add= True, blank=True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)

    class Meta:
        abstract = True




class Product(BaseModel):
    name = models.CharField(max_length = 256, default = '', blank = False) # always use blank instead of null for charfield
    description = models.TextField(max_length = 1000, default = '',blank = False)
    price = models.DecimalField(max_digits = 7, decimal_places = 2, default = '', blank = False)
    brand = models.CharField(max_length = 256, blank = True, default = 'generic')
    category = models.CharField(max_length = 30, choices = Categories.choices)
    ratings = models.DecimalField(max_digits = 3, decimal_places = 2, default = 0)
    stock = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.name