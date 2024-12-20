from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"
        fields_read_only = ('id','created_at', 'updated_at')


class OrderSerializer(serializers.ModelSerializer):

    orderItems = serializers.SerializerMethodField(method_name = 'get_order_items', read_only = True)

    class Meta:
        model = Order
        fields = "__all__"
        fields_read_only = ('id','created_at', 'updated_at')

    def get_order_items(self, obj):

        order_items = obj.orderitems.all() #orderitems is related name for OrderItems object in Order
        serializer = OrderItemSerializer(order_items, many = True)
        return serializer.data
    
