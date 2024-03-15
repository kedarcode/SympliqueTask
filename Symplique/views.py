
from django.shortcuts import render
from rest_framework.views import APIView
import dotenv
import pytz
from .helpers import *
from datetime import datetime
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist

dotenv.load_dotenv()
import requests

import os
from django.http import HttpResponseRedirect

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(self, user) :
      try:
        print(user)
        data = super().get_token(user)
        data['username']=user.email

        return data
      except ObjectDoesNotExist:
        print('Nope') 

class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class= MyTokenObtainPairSerializer
 
# Create your views here.
class AccountStuff(APIView):
  def get(self,request,uid,token):
    self_url=os.getenv('MY_URL')
    print(self_url)
    url = f'{self_url}/symplique/auth/users/activation/'  
    payload = {
        'uid':uid,
        'token': token
    }
    headers = {
            'Content-Type': 'application/json'  # Replace with the appropriate content type
        }
    response = requests.post(url,json=payload,headers=headers)
    if response.status_code >= 200 <300:
        
      return HttpResponseRedirect('http://localhost:3000/login')
    else:
        # Return an error response
        print('failed')

class ReminderView(APIView):
  Authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]
  def post(self,request):
    try:
      remindata= request.data
      if 'timezone' in remindata and remindata['timezone'] is not None and \
        validate_timezone(remindata['timezone']):
        pass
      else:
        available_timezones = get_all_timezones()
        return Response({"available_timezones": available_timezones}, status=400)
      remindata['user']=request.user.id

      timezone_str = remindata["timezone"]
      timezone = pytz.timezone(timezone_str)
      notifyon = datetime.strptime(remindata['notifyon'], "%Y-%m-%d %H:%M:%S")
      remindata['notifyon'] = timezone.localize(notifyon)
      
      addserializer= CreateReminderSerializer(data=remindata)
      if addserializer.is_valid():
        addserializer.save()
        return Response({"message":"Created"},status=200)
      else:
        return Response({"error":addserializer.errors},status=400)

    except Exception as e:
      print(e)
      return Response({'error':'inernal server error , team has been notified'},status=500)