eshop project documentation:

github link: https://github.com/ghulamabbas2/eshop

required softwares: python 3 ,vscode( install python related extensions), postgresql(pg admin) git, postman,aws,stripe



SECTION 1: starting Ecommerce API - Initial-Setup

1. create new virtual environment:
open vscode, open E:\djangop folder. create a folder eshop-django.

open eshop folder, open terminal in vscode , create virtual environment using command

E:\djangop\eshop-django> python -m venv myenv

cd myenv -> Scripts/activate to activate myenv

(myenv) PS E:\djangop\eshop-django\myenv> pip list

    Package Version

    pip 23.2.1 setuptools 65.5.0



2. create new project and add it to git hub:

E:\djangop\eshop-django> django-admin startproject eshop
this creates eshop project, inside eshop folder contains folders eshop, manage.py

E:\djangop\eshop-django> cd eshop

* create README.md file 
E:\djangop\eshop-django\eshop>echo README.md

* create requirements.txt and add packages list to it. it contains details of all python packages installed and their versions  E:\djangop\eshop-django\eshop>pip list > requirements.txt


directories inside eshop project folder:
E:\djangop\eshop-django\eshop
  
  Directory: 

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        11/21/2024   6:30 PM                eshop
-a----        11/21/2024   6:30 PM            683 manage.py
-a----        11/21/2024   6:32 PM           1120 README.md
-a----        11/21/2024   6:34 PM            666 requirements.txt


* Initialize local git repo and push it to github :
open terminal of vscode(choose powershell),type following 
E:\djangop\eshop-django\eshop> git init 
E:\djangop\eshop-django\eshop> git status 
E:\djangop\eshop-django\eshop> git add * 
E:\djangop\eshop-django\eshop> git commit -m "initial commit"

login to github account and create empty repository, copy its url 
E:\djangop\eshop-django\eshop> git branch -M main 
E:\djangop\eshop-django\eshop> git remote add origin https://github.com/karthik0237/e_shop.git 
E:\djangop\eshop-django\eshop> git remote -v 
E:\djangop\eshop-django\eshop> git push -u origin main


3. Installing packages:

E:\djangop\eshop-django\myenv> scripts/activate 
E:\djangop\eshop-django\eshop> pip install Django 
E:\djangop\eshop-django\eshop> pip install djangorestframework 

open settings.py and create separate list variables for DJANGO_APPS,LOCAL_APPS,THIRDPARTY_APPS and add 'rest_framework' to THIRDPARTY_APPS

THIRDPARTY_APPS = [ 'rest_framework',

]

LOCAL_APPS = [

]

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + LOCAL_APPS


* Installing other packages: E:\djangop\eshop-django\eshop> pip install django-filter



4. Creating config file:

 config file is nothing but a file where we keep all environment variables.
Often when working on a django project, we have some secret keys, OAuth keys and other critical information that needs to be kept safe and private. By no means should you expose such kind of keys because it makes your system vulnerable to security attacks.

Today, we are going to see how we can use python-dotenv to keep such kind of information hidden. As we can read from the docs, basically what python-dotenv does is read key-value pairs from a .env file and set them as environment variables to be retrieved later.

Environment variables are strings which contain important info like API secret keys, database credentials, passwords etc. Instead of directly putting them in settings.py file we create a .env file, put them there and get them into settings.py using import dotenv.
* 
E:\djangop\eshop-django\eshop> pip install django-dotenv
E:\djangop\eshop-django\eshop>pip list > requirements.txt (updating)

open settings.py file, and type 
* import dotenv 

#if it shows that dotenv doesnot exist then deactivate myenv and pip install python-env package globally and then again activate myenv

* In settings.py add below code:

import os 
import dotenv 

dotenv.load_dotenv()



copy and paste secretkey, debug strings in .env file, .env file: 

* SECRET_KEY = 'django-insecure-u@yp7a+iexq(-%xc7co66zy68wws6cohlevt_g^l!1zo%ual8&'
 DEBUG = True


SECRET_KEY = os.getenv('SECRET_KEY') DEBUG = os.getenv('DEBUG')

create .gitignore file, in that add lines, 
*.cpython* 
*__pycache __*
*.class 
*.env

All the files ending with above extensions will be ignored by git.

5. Connect to postgres database:

E:\djangop\eshop-django\myenv> scripts/activate

Installing package for postgresql database (myenv) PS E:\djangop\eshop-django\eshop> pip install psycopg2
pip list > requirements.txt

-> open pgadmin4 in your pc, In servers click on register server, In general tab, name=local In connection tab, hostname: localhost, port: 5432, username: postgres, password: kieb3775 and save it.

In servers, clickon local, In sub options click on databases> create database> name it as eshop-django and save it. It shows database connected successfully local/eshop-django

goto vscode In eshop-django/eshop delete db.sqlite3 file. we no longer need it.
open .env file and add:

DATABASE_NAME = 'eshop-django' 
DATABASE_USER = postgres 
DATABASE_PASSWORD = kieb3775 
DATABASE_HOST = localhost 
DATABASE_PORT = 5432

In settings.py,update below code:
DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.postgresql',
        'NAME' : os.getenv('DATABASE_NAME'),
        'USER' : os.getenv('DATABASE_USER'), 
        'PASSWORD' : os.getenv('DATABASE_PASSWORD'),
        'HOST' : os.getenv('DATABASE_HOST'), 
        'PORT' : os.getenv('DATABASE_PORT'), 
        } 
    }


* Update git: in terminal, type 
git init 
git status 
git branch init-setup
git branch

It shows two branches
*main 
init-setup

git switch init-setup 
git status 
git add * 
git commit -m "add:dotenv,packages,gitignore,postgres,requirements.txt" 
git remote -v 
git push origin init-setup

To https://github.com/karthik0237/eshop.git

[new branch] init-setup -> init-setup


(myenv) PS E:\djangop\eshop-django\eshop> python manage.py startapp product 
open settings.py and add:
 LOCAL_APPS= ['product']









 SECTION 2 : 
 
 1. creating product and base models:
 
* import inbuilt django user model: 

from django.contrib.auth.model
from django.db import models 
from django.contrib.auth.models import User



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
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True) #this field becomes null if user model is deleted.




* Apply migrations: 

(myenv) PS E:\djangop\eshop-django\eshop> python manage.py makemigrations 
(myenv) PS E:\djangop\eshop-django\eshop> python manage.py migrate


* verify tables in pgadmin4 : open pgadmin4> servers>local> rightclick and connect to local
clickon local> eshop-django> schemas> tables. you can see all the tables created by running migrations in django.


2. Create superuser and admin site: 

(myenv) PS E:\djangop\eshop-django\eshop> python manage.py createsuperuser 
username:karth 
password:root123?

(myenv) PS E:\djangop\eshop-django\eshop> python manage.py runserver

goto browser and type http://127.0.0.1:8000/admin for admin page. 

* login with username and password. In admin site users and groups are visible but not product model. To make product model visible, goto admin.py file in product app folder and add below code:

from .models import Product

admin.site.register(Product)

In admin site, open Product model and add a product, after saving its hading is shown as product object(1). To change this name, goto models.py , below inside Product class add a method:

    def str(self): 
        return self.name

3. Add serializers, views and url endpoints:

create serializers.py file in product app folder and import modelserialzer and from .models import Product  model, create base and product serializers.
Inside class meta add model mane, list of model fields and readonly fields.

In product/views.py, import api_view from rest_framework.decorators and also Response, import models and serializers also.

* create api end points using functions:

create get_products fucntion.
* @api_view(['GET'])
def get_products(request):

    # Create a variable, 
    products = Product.objects.all()       # returns all objects of product model in the form of queryset
    serializer = Productserializer(products, many = True). #serializing products to convert queryset into json format

    # Return all products as response in json format using
    retun Response({ 'products' : serializers.data })

create another fucntion to get individual product based on id or primary key. For that define get_product() fucntion with arguments (request, pk). Here pk refers to primarykey/id of a product which is given in url of getrequest.Here we want only single object from queryset. so we import and use get_object_or_404() from django.shortcuts. get_object_or_404 is a convenient shortcut function provided by Django, which is used for getting an object from a database using a model’s manager and raising an Http404 exception if the object is not found. It’s commonly used in views to get a single object based on a query and handle the case where the object doesn’t exist.


@api_view(['GET'])
def get_product(request, pk):

    product = get_object_or_404(Product, id = pk)  #returns only single object or 404 object not found error
    serializer = ProductSerializer(product, many = False)

    return Response({'product' : serializer.data})


* add urls:
In product folder create urls.py file and add code:
from . import views

urlpatterns = [

    path('products/', views.get_products, name = 'products'),
    path('products/<str:pk>', views.get_product, name =' get_product_details' ),
]


In eshop/urls.py, 
import include
urlpatterns =[path('',include('product.urls'))]


4. Postman API:

install postman, and open it, runserver copy urllink and paste it in url bar in postman app.
create a collection and name it as eshop-django, instead of typing https://127.0.0.1:8000 every time use save it as environment variable. create an environment variable with name 'DOMAIN' and add https://127.0.0.1:8000 and save it.

we can use {{DOMAIN}}/products instead of https://127.0.0.1:8000/products as a shortcut.

save 'GET' method urls in in eshop-django collection.








SECTION 3 : Filters, Search and Pagination:

1. Apply Filter for model fields:

Install django-filter from pip, in settings.py add 'django_filters' in installed apps
create a new file filters.py in the product app folder.
open it and 

 import rest_framework as filters 

 * create a class with name ProductFilter which inherits filters.FilterSet
 create meta class and add fields:

class ProdcutFilter(filters.FilterSet):

 class Meta:
    model = Product
    fields = ('category','brand')

 save it and then open views.py file:

 import Productfilter from filters.py file, in get_products function add lines:
* 
  filterset = ProductsFilter(request.GET, queryset = Product.objects.all().order_by('id'))
  serializer = ProductSerializer(filterset.qs, many = True)

  save and runserver, open postman and send get request for {{DOMAIN}}/products. In params section, add key-value as category, electronics and send it. You will see all products with electronics category only.



2. Search Product Name using keyword, price:

open filters.py inside ProductFilter class:

create fields :

keyword = filters.CharFilter(field_name = 'name', lookup_expr = 'icontains')
min_price = filters.NumberFilter(field_name = 'price' or 0, lookup_expr = 'gte')
max_price = filters.NumberFilter(field_name = 'price' or 1000000, lookup_expr = 'lte')

keyword(for name search). field_name refers to model field "name". It is taken as keyword and icontains reads each alphabet and searches in quesryset.
min_price(greater than or equal to this amount or zero )
max_price(less than or equal to this amount or 1000000 )

In meta class add above fields:
fields = ('category', 'brand', 'keyword', 'min_price', 'max_price')

open postman and runserver, in params add above fields and test results.


3. Pagination:

open views.py, and add below lines:
* 
from rest_framework import pagination

@api_view(['GET')])
def get_products(request):

    filterset = ProductsFilter(request.GET, queryset = Product.objects.all().order_by('id'))

    #serializer = ProductSerializer(products, many = True)
    resPerPage = 1             #results perpage
    paginator = pagination.PageNumberPagination()
    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(filterset.qs, request)

    serializer = ProductSerializer(queryset, many = True) #serializing products to convert queryset into json format

    return Response({'products': serializer.data}) 


runserver and open postman, send get request for /products
you will see only 2 results as we gave resperpage =2
to view secong page, in param add key = page, value= 2, it will show next page result.


If u want to know total count of poducts and resperpage, write below code in get_products:

* filterset = ProductsFilter(request.GET, queryset = Product.objects.all().order_by('id'))

    count = filterset.qs.count
    resPerPage = 2
    paginator = pagination.PageNumberPagination()
    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(filterset.qs, request)

    serializer = ProductSerializer(queryset, many = True) #serializing products to convert queryset into json format

    return Response({
        'count': count,
        'resperpage': resPerPage,
        
        'products': serializer.data}) 

* open git, stage and commit and push it to github

SECTION 4: Error and Exception Handling

1. Handle 404 and 500 errors:

In eshop project main folder create a folder utils. In utils folder, create error_views.py file and write following code:

* from django.http import JsonResponse


def handler404(request, exception):

    message = ("Route not found.")
    response = JsonResponse(data= {"error" : message})
    response.status_code = 404
    return response

def handler500(request):
    #internal server error
    message = ('Internal server error.')
    response = JsonResponse(data = {'error' : message})
    response.status_code = 500
    return response

open eshop.urls.py and add below code:

handler404 = 'utils.error_views.handler404'
handler500 = 'utils.error_views.handler500'

to test above code, in settings.py make DEBUG = False, since this works only in production
runserver and test in postman

2. Custom Exception handling code:

In utils folder create a new file, custom_exception handler.py and define a fuction with name
custom_exception handler() and write all code.

 make DEBUG = True, runserver and test in postman.

 create a new branch and post it to github.






    








