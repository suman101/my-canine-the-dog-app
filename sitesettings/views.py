from django.shortcuts import render
from .models import SMTPSetting
from .serializers import SmtpSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

class SmtpDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SmtpSerializer
    queryset = SMTPSetting.objects.all()
    lookup_field = 'id'

    
class SmtpView(ListCreateAPIView):
    serializer_class = SmtpSerializer
    queryset = SMTPSetting.objects.all()