from django.shortcuts import render
from .serializers import PasswordResetSerializers,RegisterSerializer,NewPasswordSerializers
from rest_framework import generics, serializers
from .models import UserProfile,send_mail
from .serializers import ChangePasswordSerializer, RegisterSerializer, UserProfileSerializer, EmailVerificationSerializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from .utils import Util
from django.utils.encoding import smart_bytes, smart_str, DjangoUnicodeDecodeError
from django.urls import reverse
import os
from django.shortcuts import redirect
import jwt
from django.http import HttpResponsePermanentRedirect
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from .models import User
from django.conf import settings

# Create your views here.
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )

    '''
    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "User Created Successfully. Now Perform Login to get your token",
        })

    '''

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email = user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site ='https://my-canine.herokuapp.com'
        relative_link = reverse('verify_email')
        absurl = current_site + relative_link+"?token="+str(token)
        email_body = 'Hi there '+user.username+' Use this link to verify your email: \n'+ absurl
        data = {
            'email_subject': 'Email Confirmation',
            'email_body': email_body,
            'email_receiver': user.email,
            'email_user': user.username,
        }
        Util.send_mail_register(data)
        response = {
                    'success': 'link has been sent successfully',
                    'user': user_data,
                    # 'token': str(token)
                }
        return Response(response, status=status.HTTP_201_CREATED)

class VerifyEmail(APIView):
    serializer_class = EmailVerificationSerializers

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token,key= settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            print(user)
            if not user.is_email_verified:
                user.is_email_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifer:
            return Response({'error': 'Activation Expire'}, status = status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifer:
            print(identifer)
            return Response({'error': 'Invalid Token'}, status = status.HTTP_400_BAD_REQUEST)
        
class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
     
class ChangePasswordView(generics.UpdateAPIView):
    
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    


class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializers


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        if User.objects.filter(email = email).exists():
            u = User.objects.get(email=email)
            uid64 = urlsafe_base64_encode(smart_bytes(u.id))
            token = PasswordResetTokenGenerator().make_token(u)
            # current_site = get_current_site(request= request).domain
            current_site ='https://my-canine.herokuapp.com'
            relative_link = reverse('password_token_check', kwargs={'uidb64': uid64, 'token':token})
            absurl = current_site + relative_link
            email_body = 'Hi there '+u.username+  '\n Use this link to reset your password and try not to forget another time: \n'+ absurl
            data = {
                'email_subject': 'Password Reset',
                'email_body': email_body,
                'email_receiver': u.email
            }
            Util.send_mail_register(data)
            return Response({'success': 'We have send you a mail with instructions about changing your password.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'email not registrered'},status = status.HTTP_404_NOT_FOUND)

class ResetPasswordTokenCheckView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    
    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id = id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, Please request a new one'}, status= status.HTTP_401_UNAUTHORIZED)

            return Response({'success':True, 'message':'Crendentials Valid', 'uidb64':uidb64, 'token':token, 'username':user.username}, status= status.HTTP_200_OK)


        except DjangoUnicodeDecodeError as identifer:
            return Response({'error': 'Token is not valid, Please send a new one (decode error)'}, status= status.HTTP_401_UNAUTHORIZED)



class NewPasswordView(generics.GenericAPIView):
    serializer_class = NewPasswordSerializers

    def patch(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success':True, 'message':'Password Reset completed'}, status= status.HTTP_200_OK)

    
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class UserListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "pk"

class UserUpdateView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "pk"

class UserDeleteView(generics.DestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "pk"