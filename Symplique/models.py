from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
import uuid

# Create your models here.
class UserManager(BaseUserManager):
    def create_superuser(self,email,first_name,last_name,is_admin=True,password=None):
        user = self.model(email=email,first_name=first_name,last_name=last_name,is_admin=is_admin)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email, first_name,last_name,is_active=False, is_admin=False, password=None):
            """
            Creates and saves a User with the given email, name and password.
            """
            if not email:
                raise ValueError('User must have an email address')
            user = self.model(
                email=self.normalize_email(email),
                first_name=first_name,
                last_name=last_name,
                is_active=is_active,
                is_admin=is_admin,
            )
            user.set_password(password)
            user.save(using=self._db)
            return user
        
    
class User(AbstractBaseUser):
    email= models.EmailField(max_length=255,unique=True)
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255,null=True)
    is_admin= models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    username=models.CharField(max_length=255,null=True,unique=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    

    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','is_admin']
    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name
   

    class Meta:
        db_table = 'User'
 
class Reminder(models.Model):
    CHANNELENUM = (
        ('EMAIL', 'EMAIL'),
        ('SMS', 'SMS'),
    )

    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    timezone = models.CharField(max_length=100, null=False)  
    channel= models.CharField(max_length=100,choices=CHANNELENUM,null=False)
    notifyon= models.DateTimeField(null=False,unique=True)
    message=models.TextField(null=False,blank=False)
    user=models.ForeignKey(User, models.CASCADE,related_name='user', null=False)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    class Meta:
        db_table='Reminder'