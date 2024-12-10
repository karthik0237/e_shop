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

    * Create a variable, 
    products = Product.objects.all()       # returns all objects of product model in the form of queryset
    serializer = Productserializer(products, many = True). #serializing products to convert queryset into json format

    * Return all products as response in json format using
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





SECTION 5: AWS account s3 bucket configutation, Images model, Manage Product:

create aws account using signup procedure.


1. create s3 bucket:

open aws home in search bar , type s3 , click on s3,

In s3 page, click on create bucket, give a unique name(eshop-django-udemy), uncheck block public access as this bucket is
open to public.

Bucket is created. Now click on that bucket, goto permissions and uncheck block public access and confirm and save.

In permissions tab, click on edit bucket policy, download policy.json file from udemy course, copy that code and paste it in 
bucket policy. replace your bucket name in resource value and save it.





2. User creation:

in search bar type IAM, click on IAM, create user, give a username(karthikkollurudev), click on next,
in permissions, select option "Attach policies directly" , In permission policies, search 'amazons3fullaccess' select it 
and click next, and create user.

click on that username, in security credentials tab, click on create access key, scroll down and click 'other' and clickon
create. copy both access key and security key and keep it in a safe place.

user: karthikkollurudev

access key aws : (present in aws txt file or .env file)
secret key aws : (present in aws txt file or .env file)




3. aws configuration in django:

pip install django-storages

Install boto3  package in django.pip install boto3

pip list > requirements.txt

goto settings.py and add line:
add 'storages' in Installed apps list.

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

for django version > 4.2: 
STORAGES = {

    # Media file (image) management  
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
   
    # CSS and JS file management
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}

AWS_ACCESS_KEY_ID = ''(eshop-django-udemy)
AWS_SECRET_ACCESS_KEY =''
AWS_STORAGE_BUCKET_NAME = ''
AWS_S3_SIGNATURE_VERSION = s3v4

AWS_S3_REGION_NAME = us-east-1
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = none
AWS_S3_VERIFY = True

add secret and access keys details in .env file



4. Creating images model and upload images using POST request:


im models.py add code:
* 
class ProductImages(BaseModel):

    product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True, related_name = "images")
    images = models.ImageField(upload_to = 'products') # products folder created in awss3bucket

in serializers.py create a class ProductImagesSerializer():

class ProductImagesSerializer(BaseSerializer):

    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductSerializer(BaseSerializer):

    # inorder to make image visible along with products add images field to product serializer fields.
    images = ProductImagesSerializer(many = True, read_only = True)

    class Meta:
        model = Product
        fields = ('id', 'created_at', 'updated_at', 'name', 'description', 'price', 'brand', 'category',
                  'ratings', 'stock', 'user', 'images')

In view.py add below code:
* 
     data = request.data
    files = request.FILES.getlist('images') #images is the key-value in formdata which is a model field
    print("data: ",data)
    print("files: ",files)
    # saving images into database
    images = []
    for f in files:
        image = ProductImages.objects.create(product = Product(data['product']), image = f)  
        images.append(image)

    serializer = ProductImagesSerializer(images, many = True) #retrieving images from database

    return Response({"images": serializer.data})

In urls.py add path:

path('product/upload_images', views.upload_product_images, name = "upload_product_images"),

We have created model so run migrations. We are using Imagefield so we should install Pillow package:

(myenv) PS E:\djangop\eshop-django\eshop>pip install Pillow
(myenv) PS E:\djangop\eshop-django\eshop>pip list > requirements.txt

open postman and runserver,
in body tab, clickon form-data, key-value pairs are, product:1, images:upload file from your pc, send url as POST request. you will get {"images": } details of uploaded image.
Note: files should be uploaded using forms only.

Open pgadmin4 > product_productimages and also s3aws bucket and check for images data.

5. Creating view function for product creation using POST method :

@api_view(['POST'])
def new_product(request):

def new_product(request):

    data = request.data
    serializer = ProductSerializer(data = new_product) 
#first serialize data and check whether valid or not, then omly create new object

    if serializer.is_valid():

        new_product = Product.objects.create(**data)  # multiple arguments(kwargs) i.e,we get all variables present in data.
        res = ProductSerializer(new_product, many = False)
        return Response({"new_product": res.data})
    else:
        return(serializer.errors)


add urlpath:
 path('products/new_product/', views.new_product, name = 'new_product'),


 6. Creating Update and Delete view fucntions for products:

 for updationg we use  PUT for entire object modifications, PATCH for only few fields modification
  @api_view(["PUT"])
  def update_product(request,pk):

    product = Product.get_object_or_404(id = pk)
    product.field_name = request.data['fieldname']
    '
    '
    '
    product.save()
    serializer = ProductSerializer(product, many = False)
    return Response({'product': serializer.data})

urlpatterns=[path('products/<str:pk>/update', views.update_product, name='update_product')]

for deleting product:
  @api_view(["DELETE"])
  def delete_product(request,pk):

    product = Product.get_object_or_404(id = pk)
    product.delete()
    return Resposnse("details":"deleted", status=status.200OK)
urlpatterns=[path('products/<str:pk>/delete', views.delete_product, name='update_product')]


7. Deleting images of product with signals:

in views.py, in delete_product():

#delete images along with product
    args = {"product": pk} #product field in database contains id
    images = ProductImages.objects.filter(**args)#get images with product Id
    for i in images:
        i.delete()

open models.py, cretae a fucntion:


def auto_delete_file_on_delete(sender, instance, **kwargs):

    @receiver(post_delete, sender = ProductImages)
def auto_delete_file_on_delete(sender, instance, **kwargs):

    if instance.images:     #images field verify
        instance.images.delete(save = False)






SECTION 6: Authentication

Link for simple jwt:
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

pip install djangorestframework-simplejwt

in setting.py, Installed apps = ['rest_framework_simplejwt']

add: 
* 
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ( 
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
}


from datetime import timedelta 

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours = 2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days = 2),
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.token.AccessToken",),
    "AUTH_HEADER_TYPES": ('Bearer',),
}

2. Signup and User serializers:

create new app for user login and account,

E:\djangop\eshop-django\eshop> python manage.py startapp account

open account folder and create serializers.py file,
note: we are not creating user model we are using default User model imported from django package

In serializers.py file:

from rest_framework import serializers
from django.contrib.auth.models import User


create serializer class for signup
class SignUpSerializer(models.ModelSerializer):
    model = User
    fields = ('first_name', 'last_name', 'email', 'password')

give validations using kwargs for firstname,lastname,email and password:

    extra_kwargs = {
       'first_name': {'required': True, 'allow_blank': False},

    }


create another serializer for user details using the same User model:

class UserSerializer(ModelSerializer):
    model = User
    fields = ('first_name', 'last_name', 'email', 'username')
    
* In views.py create fucntion for registering user:

#Create your views here.
@api_view(['POST'])
def register(request):

    data = request.data
    user = SignUpSerializer(data = data)

    if user.is_valid():
        if not User.objects.filter(username = data['email']).exists():
            user = User.objects.create(
                <field_name> = data['field_name'],)

            return response(201ok)

        else:
            return response(400badrequest)
    else:
    return response(user.errors)


3. Login User:

In eshop/urls.py add:

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
        

runserver and open postman type url domain/api/token, in raw/json give username and password details

you witll get access and refresh tokens, copy aceess token and open jwt.io and paste token in that website.
you will get token details. save urls for register user and generate token in postman.


4. Get Current user:

In views.py import Isauthenticated from rest_famework.permissions

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def currentuser(request):

    current_user = UserSerializer(request.user)  #request.user contains user details present in default usermodel
    return Response(current_user.data)

In urls.py, add path,   path('me/', views.currentuser, name = 'currentuser'),

copy access token, runserver, open postman, type url and send, it will give unauthorised error
In Headers, give Authorization: Bearer <access_token> and send, we get user details.

5. Save user while creating product:

In product/views.py add below lines:

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_product(request):
'
'
    if serializer.is_valid():
        new_product = Product.objects.create(**data, user = request.user)


for PUT and DELETE fucntions add below lines:
@permission_classes(['Isauthenticated'])
def fn_name(req):

    if product.user != request.user:
        return Response({"error": "You cannot update this product"}, status = 
                        status.HTTP_403_FORBIDDEN)

6. Update user profile details:

In account/views.py add lines:


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateuser(request):

    user = request.user
    data = request.data

    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.username = data['username']
    user.email = data['email']

    if data['password'] != "" :

        user.password = make_password(data['password'])

    user.save()

    serializer = UserSerializer(user, many = False)

In account/urls.py, add:

urlpatterns = [
    '
    '
    path('me/update/', views.updateuser, name = 'updateuser'),
]

save, runserver, open postman and test urls.







SECTION 7: Review model and manage product reviews

1. In product/models.py create a model class Review()
create model fields : product(foreignkey Product), user(foriegnkey User), rating(intfield), comment(textfirld)
with 
    def __str__(self):
        self.comment

In product/serializers.py create ReviewSerializer with model = Review and fields = '__all__'

python manage.py makemigrations and migrate

2. In views.py create_or_update function

@api_view(['POST'])
@permission_classes(IsAuthenticated)
def create_update_review(request,pk):

    user = request.user
    product = get_object_or_404(Product, id = pk)
    data = request.data

    review = product.reviews.filter(user = user)

    # check if rating correct or not 
    if data['rating'] not in [0,1,2,3,4,5]:

        return Response({"error": "Rating should be between 0-5 numbers only"})

    # update already existed reviews
    elif review.exists():
           here create new_review dictionary and add fields of review model(rating, comment) in dict/json format
           add them to review object using,  
           
           review.update(**new_review)

           # rating field of review model conatins individual user rating, but we want average rating of all users for
           a product. so, we need to make average of alluser ratings we use below lines:

        rating = product.reviews.aggregate(avg_ratings = Avg('rating'))   #'Avg' is imported from django.db.models

        product.ratings = rating['avg_ratings']   # ratings field is present in Product model.
        product.save()

        return Response({'detail': 'review updated'})


    #create new review object if doesnot exist already
    else:
        Review.objects.create(
                        user = user,
            product = product,
            rating = data['rating'],
            comment = data['comment']
        )
    
        # avg rating updatation is compulsory for both create and update reviews
        rating = product.reviews.aggregate(avg_ratings = Avg('rating'))

        product.ratings = rating['avg_ratings']
        product.save()

        return Response({"details": "review posted"})

    
3. adding reviews field to product model using product serializer:

class ProductSerializer(BaseSerializer):

    images = ProductImagesSerializer(many = True, read_only = True)
    reviews = serializers.SerializerMethodField(method_name = 'get_reviews', read_only = True)

    in class meta, fields list add ['reviews']

    in ProductSerializer class itself create a method with name get_fieldname:

    def get_reviews(self,obj):    # here obj is object that is being serialized
        reviews = obj.reviews.all()
        serializer = ReviewSerializer(reviews, many = True)
        return serializer.data

4. Delete review:

    in views.py ,

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request,pk):

    user = request.user
    product = get_object_or_404(Product, id = pk)
    
    review = product.reviews.filter(user = user)

    # check if review exists then, review.delete() to delete review object of Review model,
    ratings field of Product should not be null. so, if there are no rating(None), then make it as zero

    rating = product.reviews.aggregate(avg_ratings = Avg('rating'))
    if rating['avg_ratings'] is None:
            rating['avg_ratings'] = 0


    update product.ratings and save product object

    product.ratings = rating['avg_ratings']
    product.save()

    else:
    return error(review not found)

5. Add urls for reviews:

urlpatterns = [
    path('<str:pk>/reviews/', views.create_update_review, name = 'create_update_review'),
    path('<str:pk>/reviews/delete/', views.delete_review, name = 'delete_review'),
]

save all files, make migrations , migrate, runserver, test urls, save urls in postman, update requirements.txt 
init git and add new branch to github

    




SECTION 8 : EMAIL CONFIGURATION

1. gmail configuration:
 Login to ur gmail, open settings> security> enable 2-factor authentication,
 In settings, search for App passwords, create a new app with name 'eshop' and a password is created

 copy that password and open .env file, In that file add following environment variables:

 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'karthikkolluru123@gmail.com'
EMAIL_HOST_PASSWORD = **********   #paste App password here
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

In settings.py file add, all these variables, then add a line:


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#shows sent email result on console terminal screen 
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


2. Create user profile model:

 * 
 class Profile(models.Model):

    #one profile for one user
    user = models.OneToOneField(User, related_name = 'profile', on_delete = models.CASCADE)
    reset_password_token = models.CharField(max_length = 50, default = '', blank = True)
    reset_password_expire = models.DateTimeField(null = True, blank = True)

python manage.py make migrations and migrate, table is created in database. At present this table is empty
We have to write code such that whenever a user us created, a profile should also be created automatically 
for that User. To perform this task, we use a signal with sender = User model, receiver = save_profile method

In models.py file add :

#whenever a new user is registered/created, this signal automatically recieves
#that user object and create a profile object  for that user object
@receiver(post_save, sender = User)
def save_profile(sender, instance, created, **kwargs):

    user = instance  

    if created:      # created = true if user is created
        profile = Profile(user = user)
        profile.save()




3. In views.py, add lines:

from django.utils.crypto import get_random_string
from datetime import datetime, timedelta

from django.core.mail import send_mail, EmailMessage

from eshop.settings import EMAIL_HOST_USER



@api_view(['POST'])
def forgot_password(request):

    #get user object using email address provided in request.data
    data = request.data
    user = get_object_or_404(User, email = data['email])

    #create token and token expire 
     token = get_random_string(40)
    expire_date = datetime.now() + timedelta(minutes = 10)

    #save them in proile model
    user.profile.reset_password_token = token #profile is related name for Profile model object in User
    user.profile.reset_password_expire = expire_date

    user.profile.save()

3. create a function for host:

def get_current_host(request):

    protocol = request.is_secure() and 'https' or 'http'
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol = protocol, host = host)  #http://127.0.0:8000/

4. In forgot_password method:

    host = get_current_host(request)

    #create reset link
    link = "{host}reset_password/{token}".format(host = host, token = token )

    body = "Your password reset link is : {link}".format(link = link)

    send_mail("Password reset for eshop",body,"noreply@eshop.com",
               recipient_list = ["karthikkolluru123@gmail.com"], fail_silently = True)

    return Response({'details': 'Password reset email sent to: {email}'.format(email = EMAIL_HOST_USER) })

    for this mail sender = karthikkolluru123@gmail.com(email_host_user), email ids of those whom you want to receive this email should be added in recipients_list = []


5. reset_password: 

the link received in email will help to reset password for that, we have to create a view that takes password and confirmPassword data from post request, verify them and make new password and saveit in user model, 

* 
@api_view(['POST'])
def reset_password(request, token):

    data = request.data

   #profile__(double underscore)_reset_password_tokenis same as  user.profile.reset_password_token
    user  = get_object_or_404(User, profile__reset_password_token = token) 
    
  #tzinfo means timezone info set it to none to avoid any timezone related issues
  #compare reset_password_expire should be less than current time, that means time is not expired
    if user.profile.reset_password_expire.replace(tzinfo = None) < datetime.now():
        return Response({"error": "reset password token expired"})
    
    if data['password'] != data['confirmPassword']:
        return Response({"error": "passwords mismatch"})
    
    user.password = make_password(data['password'])

    #clear token and expire values in database 
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None

    user.profile.save()
    user.save()

    return Response({"details": "password reset successfully"})


6. Add urls for forgot and reset password:

 path('forgot_password/', views.forgot_password, name = 'forgot_password'),
path('reset_password/<str:token>', views.reset_password, name = 'reset_password'),

we receive this token in reset_password view

save code, runserver, open postman and test urls, we have to pass json data of 'email' for forgot password
and 'passowrd' and 'confirmPassword' for reset_password.

push code to git hub e_shop creating a branch gmail-config-forgot-reset-password






    







