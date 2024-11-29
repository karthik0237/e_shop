from django.contrib import admin
from .models import Product,ProductImages

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImages)