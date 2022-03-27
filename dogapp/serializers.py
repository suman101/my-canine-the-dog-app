from datetime import datetime as dt
from sqlite3 import Date
from rest_framework import serializers
from .models import Breed, Like, Message, PetProfile, Post, Comment, Training, Transaction
from authentication.serializers import UserSerializer

class PostListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id','caption','image','pet_name','user']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id','caption','image','pet_name','user']
        
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment','post','user','user_name']

        
class Likeserializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['userId','postId']
        
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text','image','senderId','receiverId']
        
class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id','title','description','image']
        
class PetProfileSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    
    
    class Meta:
        model = PetProfile
        fields = ['id','user','name','image','address','breed','date_of_birth','adult','age']

    def get_age(self,obj):
        d= dt.now().year-obj.date_of_birth.year
        if d<1:
            m=dt.now().month-obj.date_of_birth.month
            return str(m)+" months"

        return d

    

class TrainingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['id','title','image']


class TrainingListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    breed = BreedSerializer

    class Meta:
        model = Training
        fields = ['id','title','image','user','breed','age_limit']

    def get_breed(self,obj):
        breed = Training.objects.filter(breed=obj.id)
        return breed

        
class TrainingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    
    class Meta:
        model = Training
        fields = ['id','title','description','image','video','user']

        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['price','description','image','address','userId','phone_number']


        ############### csv file #######################

class BreedUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


        


