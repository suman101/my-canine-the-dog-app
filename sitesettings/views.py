from django.shortcuts import render
from .models import SMTPSetting
from .serializers import SmtpSerializer, ContactUsSerializers
from rest_framework import generics
from .models import ContactUs
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class SmtpDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SmtpSerializer
    queryset = SMTPSetting.objects.all()
    lookup_field = 'id'

    
class SmtpView(generics.ListCreateAPIView):
    serializer_class = SmtpSerializer
    queryset = SMTPSetting.objects.all()

############################# Contact Us views ##################################################################

class ContactUsListView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers


class ContactUsCreateView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers

    def post(self, request, *args, **kwargs):
        
        contact_serializer = ContactUsSerializers(data=request.data)
        
        if contact_serializer.is_valid():
            contact_serializer.save()
            return Response(contact_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactUsDetailView(generics.RetrieveAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers
    lookup_field = 'pk'


class ContactUsUpdateView(generics.UpdateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers
    lookup_field = 'pk'


class ContactUsDeleteView(generics.DestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers
    lookup_field = 'pk'