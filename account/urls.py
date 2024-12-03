
from django.urls import path
from . import views



urlpatterns = [

    path('register/', views.register, name = 'register_user'),
    path('me/', views.currentuser, name = 'currentuser'),
    path('me/update/', views.updateuser, name = 'updateuser'),
]