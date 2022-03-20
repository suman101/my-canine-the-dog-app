from email.policy import default
from django.db import models
from PIL import Image
from django.core.mail import send_mail 
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import AbstractUser  
# Create your models here.

class User(AbstractUser):
    """Note: User already has email, firstname , lastname, username etc.
    important mandatory field is username and password"""
    email = models.EmailField(unique=True,max_length=254)    
    phone_number = models.CharField(max_length=15,blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=100,null=True,blank=True,default=None)
    last_name = models.CharField(max_length=100,null=True,blank=True,default=None)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    is_online = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.user.username
    


class LoggedInUser(models.Model):
    user=models.OneToOneField(User,related_name='logged_in_user', on_delete=models.CASCADE)
    session_key=models.CharField(max_length=32, blank=True,null=True)


    def __str__(self):
        return self.user.username


