from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer
from Symplique.models import User

class UserCreateSerializer(UserCreateSerializer):
  class Meta(UserCreateSerializer.Meta):
    model=User
    fields=('email','first_name','last_name','password')
  
class CreateReminderSerializer(serializers.ModelSerializer):
  class Meta:
      model=Reminder
      fields='__all__'