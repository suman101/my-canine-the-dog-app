from rest_framework import serializers
from .models import SMTPSetting

class SmtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMTPSetting
        fields = ['id','email_host_user','email_host_password','email_port']