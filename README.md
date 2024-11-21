eshop project documentation:

github link: https://github.com/ghulamabbas2/eshop

required softwares: python 3 vscode( install python related extensions) postgresql(pg admin) git postman



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

* SECRET_KEY = r'django-insecure-u@yp7a+iexq(-%xc7co66zy68wws6cohlevt_g^l!1zo%ual8&'
 DEBUG = True

(note: r'' indicates rawstring which means sequences like \n,\t,%s etc are ignored )
and call them in settings.py like below:

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
