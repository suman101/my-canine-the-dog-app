from django.db import models
from django.core import exceptions


class SMTPSetting(models.Model):
    email_port = models.IntegerField(default=587)
    email_host = models.CharField(max_length=100,blank=True, null=True)
    email_host_user = models.EmailField(blank=True, null=True)
    email_host_password = models.CharField(max_length=200,blank=True, null=True, help_text="Use the app password not your actual password for the security reason.")

    def __str__(self):
        return f'{self.email_host_user}'

    def save(self,*args,**kwargs):
        if not self.pk and SMTPSetting.objects.exists():
            raise exceptions.PermissionDenied('create action not allowed')
        return super(SMTPSetting, self).save(*args,**kwargs)
    
    def delete(self):
        raise exceptions.PermissionDenied('delete action not allowed')

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    email = models.EmailField(max_length=50)
    country = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
