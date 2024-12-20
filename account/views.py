from django.shortcuts import render, get_object_or_404
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta

from django.core.mail import send_mail, EmailMessage

from eshop.settings import EMAIL_HOST_USER

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Profile
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
                password = make_password(data['password']), #turn plain-text password into hash for database storage
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

    current_user = UserSerializer(request.user)  #request.user conatins User model fields
    
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




def get_current_host(request):

    protocol = request.is_secure() and 'https' or 'http'
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol = protocol, host = host)



@api_view(['POST'])
def forgot_password(request):

    data = request.data

    user = get_object_or_404(User, email = data['email'])

    token = get_random_string(40)
    expire_date = datetime.now() + timedelta(minutes = 10)

    user.profile.reset_password_token = token #profile is related name for Profile model object in User
    user.profile.reset_password_expire = expire_date

    user.profile.save()

    host = get_current_host(request)
    link = "{host}reset_password/{token}".format(host = host, token = token )

    body = "Your password reset link is : {link}".format(link = link)

    send_mail("Password reset for eshop",body,"noreply@eshop.com",
               recipient_list = ["karthikkolluru123@gmail.com"], fail_silently = True)

    return Response({'details': 'Password reset email sent to: {email}'.format(email = EMAIL_HOST_USER) })



@api_view(['POST'])
def reset_password(request, token):

    data = request.data
    user  = get_object_or_404(User, profile__reset_password_token = token) #profile__(double underscore)_reset_password_token
    # is same as  user.profile.reset_password_token

    if user.profile.reset_password_expire.replace(tzinfo = None) < datetime.now():
        return Response({"error": "reset password token expired"})
    
    if data['password'] != data['confirmPassword']:
        return Response({"error": "passwords mismatch"})
    
    user.password = make_password(data['password'])
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None

    user.profile.save()
    user.save()

    return Response({"details": "password reset successfully"})


