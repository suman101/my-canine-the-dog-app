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
from dogapp.models import PetProfile



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    confirm_password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = [ 'email', 'username', 'password' , 'confirm_password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('passwords should be same')
        if not username.isalnum():
            raise serializers.ValidationError({'username': 'The username should only contain only alphanumeric value'})
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    

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
            'email',
            'first_name',
            'last_name',
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
    

class PasswordResetSerializers(serializers.Serializer):
    email = serializers.EmailField(max_length=256, min_length=2)

    class Meta:
        fields = ['email']

class NewPasswordSerializers(serializers.Serializer):
    password = serializers.CharField(max_length=68,min_length=2, write_only= True)
    token = serializers.CharField(min_length=1, write_only= True)
    uidb64 = serializers.CharField(min_length=1, write_only= True)

    class Meta:
        fields = ['password','token', 'uidb64']


    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id = id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)   

    
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    pet_user = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id','user','contact', 'address','is_online','pet_user']

    def get_pet_user(self,obj):
        pet_user=PetProfile.objects.filter(user=obj.id).values()
        
        return pet_user




