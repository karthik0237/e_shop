from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from product.models import Product
from .models import *
from .serializers import OrderSerializer
from .filters import OrdersFilter

import os
import stripe
from account.views import get_current_host


# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_orders(request):

    filterset = OrdersFilter(request.GET, queryset = Order.objects.all().order_by('id'))
    count = filterset.qs.count()

    #pagination
    resPerPage = 3
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage
    queryset = paginator.paginate_queryset(filterset.qs, request)

    serializer = OrderSerializer(queryset, many = True)

    return Response({
        "count": count,
        "resPerPage": resPerPage,
        "orders": serializer.data})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_single_order(request, pk):

    order = get_object_or_404(Order, id = pk)
    serializer = OrderSerializer(order, many = False)

    return Response({"order": serializer.data})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_order(request):

    user = request.user
    data = request.data

    order_items = data['orderItems']

    if order_items and len(order_items) == 0:
        return Response({'error': 'No Order Items. Please add atleast one product'}, status = status.HTTP_400_BAD_REQUEST)
    
    else:

        # create order

        total_amount = sum(item['price'] * item['quantity'] for item in order_items)
        order = Order.objects.create(
            user = user,
            street = data['street'],
            city = data['city'],
            state = data['state'],
            zip_code = data['zip_code'],
            phone_no = data['phone_no'],
            country = data['country'],
            total_amount = total_amount
        )

        # create order items and set order to order items
        for i in order_items:
           product = Product.objects.get(id = i['product'])

           item = OrderItem.objects.create(
                product = product,
                order = order,
                name = product.name,
                quantity = i['quantity'],
                price = i['price'],
           )

        #update product stock
        product.stock = product.stock - item.quantity
        product.save()
    
        serializer = OrderSerializer(order, many = False)

        return Response(serializer.data)
        


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_order(request, pk):

    user = request.user

    if user.is_staff is True:        #for admin 'is_staff' == True or u can use [IsAdminUser] class
        order = get_object_or_404(Order, id=pk)
        order.order_status = request.data['order_status']

        serializer = OrderSerializer(order, many = False)

        return Response({"order": serializer.data})
    else:
        return Response({"error": "only admin is allowed to perform this task"}, status = status.HTTP_403_FORBIDDEN)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_order(request, pk):

    order = get_object_or_404(Order, id=pk)
    order.delete()

    return Response({"details": "order deleted"})




stripe.api_key = os.getenv("STRIPE_PRIVATE_KEY")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_checkout_session(request):

    user = request.user
    data = request.data
    YOUR_DOMAIN = str(get_current_host(request))

    order_items = data["orderItems"]
    shipping_details = {
        'street': data['street'],
        'city': data['city'],
        'state': data['state'],
        'zip_code': data['zip_code'],
        'phone_no': data['phone_no'],
        'country': data['country'],
        'user': user.id
    }

    checkout_order_items = []
    for item in order_items:

        checkout_order_items.append({
            'price_data' : {
                'currency': 'INR',
                'product_data': {
                    'name': item['name'],
                    'images': [item['image']],   #we have to add 'image' field in orderitems model
                    'metadata': {'product_id': item['product']}
                },
                'unit_amount': item['price'] * 100
            },

            'quantity': item['quantity']
        } )

    session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        metadata = shipping_details,
        line_items = checkout_order_items,
        customer_email = user.email,
        mode = 'payment',
        success_url = YOUR_DOMAIN,
        cancel_url = YOUR_DOMAIN
    )

    return Response({'session': session})
