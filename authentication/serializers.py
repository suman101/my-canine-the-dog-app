from .models import UserProfile
from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims

        token['username'] = user.username
        return token
    '''

    """
    For login user
    """
    default_error_messages = {
        'no_active_account': 'Username or Password does not matched.'
    }

    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)

        # Add custom claims
        obj=User.objects.get(id=user.id)
        token['user'] = user.username
        token['email'] = obj.email
        
        if user is None:
            raise serializers.ValidationError("User is not registered")
        return token

    def validate(self, attrs):
        #email = attrs.get('email')
        username = attrs.get('username')
        password = attrs.get('password')
        try:
            us = User.objects.get(email__iexact=attrs.get("username"))
            username = us.username
        except Exception as e:
            pass

        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid Crendential, Try again')
        refresh = self.get_token(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        return {
            'access': access_token,
            'refresh': refresh_token,
        }



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email','first_name','last_name']
        
        extra_kwargs = {
            'password': {'write_only':True},
        }
        
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'], first_name=validated_data['first_name'], last_name=validated_data['last_name'],email=validated_data['email'])
        return user

class EmailVerificationSerializers(serializers.ModelSerializer):
    tokens = serializers.CharField(max_length=555, help_text="Enter same email as you have provided during regristrations")

    class Meta:
        model = User
        fields = ['tokens']
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )
    
class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['password','password2','old_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
    
class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']
        
class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)
    
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id','user','contact', 'address', 'profile_pic','is_online']