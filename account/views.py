from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout, authenticate, login
from main.models import *
from main.serializers import *
from .token import *




@api_view(['POST'])
def signin_view(request):
   username = request.POST.get('username')
   password = request.POST.get('password')
   try:
       usr = authenticate(username=username, password=password)
       use = request.user
       try:
           if usr is not None:
               status = 200
               tokens = get_tokens_for_user(use)
               data = {
                   "status": status,
                   "username": username,
                   "token": tokens,
               }
           else:
               status = 403
               message =" Invalid Password or username "
               data = {
                   "status": status,
                   "message": message,
               }
       except User.DoesnotExist:
           status =404
           message = " This User is not defined! "
           data = {
             "status": status,
               "message":message,
           }



       return Response(data)
   except Exception as err:
       return Response(f'{err}')


@api_view(["POST"])
def signup_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    new = User.objects.create_user(username=username, password=password)
    ser = UserSerializers(new)
    return Response(ser.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'data':'sucses'})