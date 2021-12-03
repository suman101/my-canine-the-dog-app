from django.shortcuts import render
from .serializers import BreedSerializer, Likeserializer, MessageSerializer, PetProfileSerializer, PostSerializer, CommentSerializer, TrainingSerializer, TransactionSerializer
from rest_framework import generics
from .models import PetProfile, Post, Comment, Like, Message, Breed, Training, Transaction
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def post(self, request, *args, **kwargs):

      post_serializer = PostSerializer(data=request.data)

      if post_serializer.is_valid():
          post_serializer.save()
          return Response(post_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = Likeserializer
    
class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = Likeserializer
    
class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def post(self, request, *args, **kwargs):

      message_serializer = MessageSerializer(data=request.data)

      if message_serializer.is_valid():
          message_serializer.save()
          return Response(message_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
class MessageDeleteView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
class BreedListView(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    
class BreedCreateView(generics.CreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    
    def post(self, request, *args, **kwargs):

      breed_serializer = BreedSerializer(data=request.data)

      if breed_serializer.is_valid():
          breed_serializer.save()
          return Response(breed_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(breed_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BreedDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    
class BreedDeleteView(generics.DestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    
class PetProfileListView(generics.ListAPIView):
    queryset = PetProfile.objects.all()
    serializer_class = PetProfileSerializer
    
class PetProfileCreateView(generics.CreateAPIView):
    queryset = PetProfile.objects.all()
    serializer_class = PetProfileSerializer
    
class PetProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetProfile.objects.all()
    serializer_class = PetProfileSerializer
    
class PetProfileDeleteView(generics.DestroyAPIView):
    queryset = PetProfile.objects.all()
    serializer_class = PetProfileSerializer
    
class TrainingListView(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    
class TrainingCreateView(generics.CreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    
    def post(self, request, *args, **kwargs):

      training_serializer = TrainingSerializer(data=request.data)

      if training_serializer.is_valid():
          training_serializer.save()
          return Response(training_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(training_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class TrainingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    
class TrainingDeleteView(generics.DestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    
class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    def post(self, request, *args, **kwargs):

      transaction_serializer = TransactionSerializer(data=request.data)

      if transaction_serializer.is_valid():
          transaction_serializer.save()
          return Response(transaction_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    
class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
class TransactionDeleteView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    
    
    
    
    

    
    

    

    
      


