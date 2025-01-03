from django.db import models
from django.contrib.auth.models import User


from product.models import Product



class OrderStatus(models.TextChoices):
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'


class PaymentStatus(models.TextChoices):
    PAID = 'PAID'
    UNPAID = 'UNPAID'


class PaymentMode(models.TextChoices):
    COD = 'COD'
    CARD = 'CARD'



# Create your models here.
class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)

    class Meta:
        abstract = True


class Order(BaseModel):

    street = models.CharField(max_length = 256, default = '', blank = False)
    city = models.CharField(max_length = 100, default = '', blank = False)
    state = models.CharField(max_length = 100, default = '', blank = False)
    zip_code = models.CharField(max_length = 100, default = '', blank = False)
    phone_no = models.CharField(max_length = 32, default = '', blank = False)
    country = models.CharField(max_length = 100, default = '', blank = False)
    total_amount = models.DecimalField(max_digits = 7, decimal_places = 2, default = '', blank = False)
    payment_status = models.CharField(
        max_length = 20, 
        choices = PaymentStatus.choices, 
        default = PaymentStatus.UNPAID
        )
    order_status = models.CharField(
        max_length = 20, 
        choices = OrderStatus.choices, 
        default = OrderStatus.PROCESSING
        )
    payment_mode = models.CharField(
        max_length = 20, 
        choices = PaymentMode.choices,
        default = PaymentMode.COD
        )
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)


    def __str__(self):
        return str(self.id)


class OrderItem(BaseModel):

    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.CASCADE, null = True, related_name = 'orderitems')
    name = models.CharField(max_length = 200, default = '', blank = False)
    quantity = models.IntegerField(default =1)
    price = models.DecimalField(max_digits = 7, decimal_places = 2, default = '', blank = False)
    image = models.CharField(max_length = 500, default = '', blank = False) #adding image aws url

    def __str__(self):
        return self.name
    