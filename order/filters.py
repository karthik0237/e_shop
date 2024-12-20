from django_filters import rest_framework as filters

from .models import Order, OrderItem


class OrdersFilter(filters.FilterSet):


    class Meta:
        model = Order
        fields = ('id', 'order_status', 'payment_status', 'payment_mode')