from rest_framework import serializers
from .models import Breed, Like, Message, PetProfile, Post, Comment, Training, Transaction

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user','caption','image']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment','post','user']
        
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
        fields = ['title','description','image']
        
class PetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetProfile
        fields = ['name','address','breed','date_of_birth']
        
class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['title','description','image','video']
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['price','description','image','address','userId','phone_number']
        


