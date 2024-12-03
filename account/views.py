from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import SignUpSerializer, UserSerializer

# Create your views here.
@api_view(['POST'])
def register(request):

    data = request.data
    user = SignUpSerializer(data = data)

    if user.is_valid():
        if not User.objects.filter(username = data['email']).exists():
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                password = make_password(data['password']),
                username = data['email']
            )

            return Response({"details": "user registered successfully"}, status=status.HTTP_201_CREATED)
        
        else:
            return Response({"error": "user already exists"}, status = status.HTTP_400_BAD_REQUEST)


    else:
        return Response(user.errors)





@api_view(["GET"])
@permission_classes([IsAuthenticated])
def currentuser(request):

    current_user = UserSerializer(request.user)
    
    return Response(current_user.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateuser(request):

    user = request.user
    data = request.data

    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.username = data['username']
    user.email = data['email']

    if data['password'] != "" :

        user.password = make_password(data['password'])

    user.save()

    serializer = UserSerializer(user, many = False)

    return Response({"details": "successfully updated"})