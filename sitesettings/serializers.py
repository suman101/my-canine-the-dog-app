from rest_framework import serializers
from .models import SMTPSetting, ContactUs

class SmtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMTPSetting
        fields = ['id','email_host_user','email_host_password','email_port']

class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id','name','phone_number','message','email','country','created_at','updated_at']