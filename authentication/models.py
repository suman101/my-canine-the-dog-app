from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.mail import send_mail 
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(upload_to = 'images', default= 'default.png',null=True,blank=True)
    is_online = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user
    
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
