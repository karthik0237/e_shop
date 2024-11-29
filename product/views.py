from django.shortcuts import render, get_object_or_404
from rest_framework import status, pagination

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, ProductImages
from .serializers import ProductSerializer, ProductImagesSerializer
from .filters import ProductsFilter




# Create your views here.

#get all products
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


# get single product based on Id
@api_view(['GET'])
def get_product(request, pk):

    product = get_object_or_404(Product, id = pk)  # returns only single object or 404 object not found error
    serializer = ProductSerializer(product, many = False)

    return Response({'product' : serializer.data})


#create a new product
@api_view(['POST'])
def new_product(request):

    data = request.data
    serializer = ProductSerializer(data = data) 
#first serialize data and check whether valid or not, then omly create new object
    if serializer.is_valid():

        new_product = Product.objects.create(**data)  # multiple arguments(kwargs) i.e,we get all variables present in data.
        res = ProductSerializer(new_product, many = False)
        return Response({"new_product": res.data})
    else:
        return(serializer.errors)




 # for updationg we use  PUT for entire object modifications, PATCH for only few fields modification
@api_view(["PUT"])
def update_product(request,pk):

#name', 'description', 'price', 'brand', 'category', 'ratings', 'stock
    product = get_object_or_404(Product, id = pk)
    product.name = request.data['name']
    product.description = request.data['description']
    product.price = request.data['price']
    product.brand = request.data['brand']
    product.category = request.data['category']
    product.ratings = request.data['ratings']
    product.stock = request.data['stock']

    product.save()
    serializer = ProductSerializer(product, many = False)
    return Response({'product': serializer.data})


# for deleting product:
@api_view(["DELETE"])
def delete_product(request,pk):

    product = get_object_or_404(Product, id = pk)

    #check if user is same - todo

    #delete images along with product
    args = {"product": pk} #product field in database contains id
    images = ProductImages.objects.filter(**args)#get images with product Id
    for i in images:
        i.delete()

    product.delete()

    return Response({'detials': 'Product is deleted'}, status = status.HTTP_200_OK)


# upload product images
@api_view(['POST'])
def upload_product_images(request):

    data = request.data
    '''request data contains data that we give while sending post request. In this case we gave form data,
    product: (product ID), images:(uploaded from pc)'''
    files = request.FILES.getlist('images') #images is the key-value in formdata which is a model field
    '''Note that request.FILES will only contain data if the request method was POST, 
    at least one file field was actually posted, and 
    the <form> that posted the request has the attribute enctype="multipart/form-data".
      Otherwise, request.FILES will be empty. Files are sent in html form-data only.'''
    print("data: ",data)
    print("files: ",files)
    # saving images into database
    images = []
    for f in files:
        image = ProductImages.objects.create(product = Product(data['product']), image = f)  
        images.append(image)

    serializer = ProductImagesSerializer(images, many = True) #retrieving images from database

    return Response({"images": serializer.data})
