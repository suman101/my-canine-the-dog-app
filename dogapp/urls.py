from django.urls import path
from .views import LikeCreateView, LikeDeleteView, MessageCreateView, MessageDeleteView, MessageDetailView, MessageListView, PetProfileCreateView, PetProfileDeleteView, PetProfileDetailView, PetProfileListView, PostListView,PostCreateView,PostDetailView,PostDeleteView, CommentListView,CommentCreateView,CommentDetailView, CommentDeleteView, TrainingCreateView, TrainingDeleteView, TrainingDetailView, TrainingListView, TransactionCreateView, TransactionDeleteView, TransactionDetailView, TransactionListView

urlpatterns = [
    path('post/', PostListView.as_view()),
    path('postcreate/', PostCreateView.as_view()),
    path('postdetail/', PostDetailView.as_view()),
    path('postdelete/', PostDeleteView.as_view()),
    
    path('comment/', CommentListView.as_view()),
    path('commentcreate/', CommentCreateView.as_view()),
    path('commentdetail/<int:pk>', CommentDetailView.as_view()),
    path('commentdelete/<int:pk>', CommentDeleteView.as_view()),
    
    path('likecreate/', LikeCreateView.as_view()),
    path('likedelete/<int:pk>', LikeDeleteView.as_view()),
    
    path('message/', MessageListView.as_view()),
    path('messagecreate/', MessageCreateView.as_view()),
    path('messagedetail/<int:pk>/', MessageDetailView.as_view()),
    path('messagedelete/<int:pk>/', MessageDeleteView.as_view()),
    
    path('petprofile/', PetProfileListView.as_view()),
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
    path('transaction-delete/<int:pk>', TransactionDeleteView.as_view()),
    
]