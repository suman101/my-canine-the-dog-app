from django.contrib import admin
from .models import SMTPSetting, ContactUs
# Register your models here.

admin.site.register(SMTPSetting)
admin.site.register(ContactUs)
