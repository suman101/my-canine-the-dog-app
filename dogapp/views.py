from django.shortcuts import render
from .serializers import BreedSerializer, Likeserializer, MessageSerializer, PetProfileSerializer, PostSerializer, CommentSerializer, TrainingSerializer, TransactionSerializer,PostListSerializer,TrainingListSerializer,TrainingCategorySerializer,BreedUploadSerializer
from rest_framework import generics
from .models import PetProfile, Post, Comment, Like, Message, Breed, Training, Transaction,TrainingCategory
from rest_framework.response import Response
from rest_framework import status
from .paginations import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import UserProfile
from django.http import QueryDict



# Create your views here.
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['user__username',]
    ordering_fields = ['created',]
    permission_classes = [IsAuthenticated]


    
    
class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    '''
    def post(self, request, *args, **kwargs):

        serializer = PostSerializer(data=request.data)
        print(request.user)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Post added successfully',
                'user': serializer.data
            }
            return Response(response, status=status_code)
        else:
            response = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status_code)
   '''
    
    '''
    def post(self, request, *args, **kwargs):

      post_serializer = PostSerializer(data=request.data)
      print(post_serializer)

      if post_serializer.is_valid():
          
          
          post_serializer.save()
          return Response(post_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    '''

    def post(self, request):
        try:
            user = UserProfile.objects.get(user=self.request.user.id)
            print(user)
            username = UserProfile.objects.get(user=self.request.user)
            print(username)
            user_id=user.id
            data = {
                #'post':request.data['post'],
                'username':username.user.username,
                'user_id': user_id,                
                'caption': request.data['caption'],
                'pet_name': request.data['pet_name'],
                'image': request.data['image'],
                                          
            }
            print(data)
            query_dict = QueryDict('', mutable=True)
            query_dict.update(data)
            serializer = PostSerializer(data=query_dict)
            valid = serializer.is_valid(raise_exception=True)
            if valid:
                serializer.save()
                status_code = status.HTTP_201_CREATED
                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'post added successfully',
                    'user': serializer.data
                }
        
                return Response(response, status=status_code)
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(serializer.errors, status=status_code)
        except ObjectDoesNotExist:
            raise Http404("Cannot created, Please Login to add post")

      
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    
class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

class PostListPersonal(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.kwargs.get('user_id'))




class CreateReadCommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return super().get_queryset().filter(post=self.kwargs.get('post_id'))
    
class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.kwargs.get('username'))
    
class CommentCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = UserProfile.objects.get(user=self.request.user.id)
                
            user_id=user.id
            data = {
                'post':request.data['post'],
                'user_name':request.data['user_name'],
                'user': user_id,                
                'comment': request.data['comment'],

                                          
            }
            print(data)
            query_dict = QueryDict('', mutable=True)
            query_dict.update(data)
            serializer = CommentSerializer(data=query_dict)
            valid = serializer.is_valid(raise_exception=True)
            if valid:
                serializer.save()
                status_code = status.HTTP_201_CREATED
                response = {
                    'success': True,
                    'statusCode': status_code,
                    'message': 'comment added successfully',
                    'user': serializer.data
                }
        
                return Response(response, status=status_code)
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                return Response(serializer.errors, status=status_code)
        except ObjectDoesNotExist:
            raise Http404("Cannot created, Please Login to add comment")
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    
class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    
class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = Likeserializer
    
class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = Likeserializer
    
class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = PageNumberPagination
    
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
    lookup_field = 'pk'
    
class MessageDeleteView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'pk'
    
class BreedListView(generics.ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    pagination_class = PageNumberPagination
    
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
    lookup_field = 'pk'
    
class BreedDeleteView(generics.DestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    lookup_field = 'pk'
    
class PetProfileListView(generics.ListAPIView):
    queryset = PetProfile.objects.all()
    serializer_class = PetProfileSerializer
    pagination_class = PageNumberPagination
    
class PetProfileCreateView(generics.CreateAPIView):
    queryset = PetProfile.objects.all()
    serializer_class = PetProfileSerializer

    def post(self, request, *args, **kwargs):

        serializer = PetProfileSerializer(data=request.data)
        print(request.user)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Post added successfully',
                'user': serializer.data
            }
            return Response(response, status=status_code)
        else:
            response = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status_code)

    
    
class PetProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetProfile.objects.all()
    serializer_class = PetProfileSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.kwargs.get('user_id'))


    
class PetProfileDeleteView(generics.DestroyAPIView):
    queryset = PetProfile.objects.all()
    serializer_class = PetProfileSerializer
    lookup_field = 'pk'

class TrainingCategoryEachView(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingCategorySerializer

    def get_queryset(self):
        return super().get_queryset().filter(category=self.kwargs.get('category_id'))

class TrainingCategoryListView(generics.ListAPIView):
    queryset = TrainingCategory.objects.all()
    serializer_class = TrainingCategorySerializer

class TrainingCategoryCreateView(generics.ListAPIView):
    queryset = TrainingCategory.objects.all()
    serializer_class = TrainingCategorySerializer

class TrainingCategoryDetailView(generics.ListAPIView):
    queryset = TrainingCategory.objects.all()
    serializer_class = TrainingCategorySerializer
    lookup_field = 'pk'

class TrainingCategoryDeleteView(generics.ListAPIView):
    queryset = TrainingCategory.objects.all()
    serializer_class = TrainingCategorySerializer
    lookup_field = 'pk'
    
class TrainingListView(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingListSerializer
    pagination_class = PageNumberPagination
    
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
    lookup_field = 'pk'
    
class TrainingDeleteView(generics.DestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    lookup_field = 'pk'
    
class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = PageNumberPagination
    
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
    lookup_field = 'pk'
    
class TransactionDeleteView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'pk'




class UploadFileView(generics.CreateAPIView):
    serializer_class = BreedUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = Breed(
                       id = row['id'],
                       title=row['Title'],
                       description=row['Description'],
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
    

    
    
    
    
    
    

    
    

    

    
      


