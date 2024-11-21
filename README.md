eshop project documentation:

github link: https://github.com/ghulamabbas2/eshop

required softwares: python 3 vscode( install python related extensions) postgresql(pg admin) git postman

SECTION 1: starting Ecommerce API - Initial-Setup

create new virtual environment:
open vscode, open E:\djangop folder. create a folder eshop-django.

open eshop folder, open terminal in vscode , create virtual environment using command

E:\djangop\eshop-django> python -m venv myenv

cd myenv -> Scripts/activate to activate myenv

(myenv) PS E:\djangop\eshop-django\myenv> pip list

Package Version

pip 23.2.1 setuptools 65.5.0

create new project and add it to git hub:
E:\djangop\eshop-django> django-admin startproject eshop

this creates eshop project, inside eshop folder contains folders eshop, manage.py

E:\djangop\eshop-django> cd eshop

create README.md file E:\djangop\eshop-django\eshop>echo README.md

create requirements.txt and add packages list to it. it contains details of all python packages installed and their versions E:\djangop\eshop-django\eshop>pip list > requirements.txt


directories inside eshop project folder:

    Directory: E:\djangop\eshop-django\eshop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        11/21/2024   6:30 PM                eshop
-a----        11/21/2024   6:30 PM            683 manage.py
-a----        11/21/2024   6:32 PM           1120 README.md
-a----        11/21/2024   6:34 PM            666 requirements.txt

* Initialize local git repo and push it to github :
open terminal of vscode(choose powershell),type following E:\djangop\eshop-django\eshop> git init E:\djangop\eshop-django\eshop> git status E:\djangop\eshop-django\eshop> git add * E:\djangop\eshop-django\eshop> git commit -m "initial commit"

login to github account and create empty repository, copy its url E:\djangop\eshop-django\eshop> git branch -M main E:\djangop\eshop-django\eshop> git remote add origin https://github.com/karthik0237/eshop.git E:\djangop\eshop-django\eshop> git remote -v E:\djangop\eshop-django\eshop> git push -u origin main