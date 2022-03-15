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

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(upload_to = 'images/',default='images/avatar.png/',null=True,blank=True)
    is_online = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

        img=Image.open(self.profile_pic.path)

        if img.height>400 or img.width>400:
            output_size=(400,400)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
            
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )


class LoggedInUser(models.Model):
    user=models.OneToOneField(User,related_name='logged_in_user', on_delete=models.CASCADE)
    session_key=models.CharField(max_length=32, blank=True,null=True)


    def __str__(self):
        return self.user.username


