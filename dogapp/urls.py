from django.urls import path
from .views import LikeCreateView, LikeDeleteView, MessageCreateView, MessageDeleteView, MessageDetailView, MessageListView, PetProfileCreateView, PetProfileDeleteView, PetProfileDetailView, PetProfileListView, PostListView,PostCreateView,PostDetailView,PostDeleteView, CommentListView,CommentCreateView,CommentDetailView, CommentDeleteView, TrainingCreateView, TrainingDeleteView, TrainingDetailView, TrainingListView, TransactionCreateView, TransactionDeleteView, TransactionDetailView, TransactionListView, CreateReadCommentView, PostListPersonal

urlpatterns = [
    path('post-list/', PostListView.as_view()),
    path('post-create/', PostCreateView.as_view()),
    path('post-detail/<int:pk>/', PostDetailView.as_view()),
    path('post-delete/<int:pk>/', PostDeleteView.as_view()),
    path('post/<int:post_id>/comments/', CreateReadCommentView.as_view()),
    path('post/<int:user_id>/', PostListPersonal.as_view()),
    
    path('comment-list/', CommentListView.as_view()),
    path('comment-create/', CommentCreateView.as_view()),
    path('comment-detail/<int:pk>/', CommentDetailView.as_view()),
    path('comment-delete/<int:pk>/', CommentDeleteView.as_view()),
    
    path('like-create/', LikeCreateView.as_view()),
    path('like-delete/<int:pk>/', LikeDeleteView.as_view()),
    
    path('message-list/', MessageListView.as_view()),
    path('message-create/', MessageCreateView.as_view()),
    path('message-detail/<int:pk>/', MessageDetailView.as_view()),
    path('message-delete/<int:pk>/', MessageDeleteView.as_view()),
    
    path('petprofile-list/', PetProfileListView.as_view()),
    path('petprofile-create/', PetProfileCreateView.as_view()),
    path('petprofile-detail/<int:pk>/', PetProfileDetailView.as_view()),
    path('petprofile-delete/<int:pk>/', PetProfileDeleteView.as_view()),
    
    path('training/', TrainingListView.as_view()),
    path('training-create/', TrainingCreateView.as_view()),
    path('training-detail/<int:pk>/', TrainingDetailView.as_view()),
    path('training-delete/<int:pk>/', TrainingDeleteView.as_view()),
    
    path('transaction/', TransactionListView.as_view()),
    path('transaction-create/', TransactionCreateView.as_view()),
    path('transaction-detail/<int:pk>/', TransactionDetailView.as_view()),
    path('transaction-delete/<int:pk>/', TransactionDeleteView.as_view()),
    
]