
from django.urls import path
from . import views



urlpatterns = [
    
    path('register/', views.register, name = 'register_user'),
    path('me/', views.currentuser, name = 'currentuser'),
    path('me/update/', views.updateuser, name = 'updateuser'),

    path('forgot_password/', views.forgot_password, name = 'forgot_password'),
    path('reset_password/<str:token>', views.reset_password, name = 'reset_password'),
]