from django.urls import path

from . import views


urlpatterns = [

    path('orders/new/', views.new_order, name = 'new_order'),
    path('orders/', views.get_all_orders, name = 'get_all_orders'),
    path('orders/<str:pk>/', views.get_single_order, name = 'get_single_order'),
    path('orders/<str:pk>/update/', views.update_order, name = 'update_order'),
    path('orders/<str:pk>/delete/', views.delete_order, name = 'delete_order'),

]