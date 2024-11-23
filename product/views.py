from django.shortcuts import render, get_object_or_404
from rest_framework import status, pagination

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from .filters import ProductsFilter




# Create your views here.
@api_view(['GET'])
def get_products(request):

    filterset = ProductsFilter(request.GET, queryset = Product.objects.all().order_by('id'))
    #products = Product.objects.all()       # returns all objects of product model in the form of queryset
    #serializer = ProductSerializer(products, many = True)
    count = filterset.qs.count()
    resPerPage = 2
    paginator = pagination.PageNumberPagination()
    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(filterset.qs, request)

    serializer = ProductSerializer(queryset, many = True) #serializing products to convert queryset into json format

    return Response({
        'count': count,
        'resperpage': resPerPage,
        
        'products': serializer.data}) 



@api_view(['GET'])
def get_product(request, pk):

    product = get_object_or_404(Product, id = pk)  #returns only single object or 404 object not found error
    serializer = ProductSerializer(product, many = False)

    return Response({'product' : serializer.data})


