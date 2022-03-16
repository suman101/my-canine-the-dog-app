from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterApi, LogoutView,  ChangePasswordView, GoogleLogin, UserListView, UserDetailView, UserUpdateView, UserDeleteView, VerifyEmail,PasswordResetView,ResetPasswordTokenCheckView,NewPasswordView

urlpatterns = [
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/register/', RegisterApi.as_view()),
    path('email-verify/', VerifyEmail.as_view(), name='verify_email'),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset/<uidb64>/<token>/', ResetPasswordTokenCheckView.as_view(),name = 'password_token_check'),
    path('password-reset-complete/', NewPasswordView.as_view()),
    
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    
    path('user-list/', UserListView.as_view()),
    path('user-detail/<int:pk>/', UserDetailView.as_view()),
    path('user-update<int:pk>/', UserUpdateView.as_view()),
    path('user-delete<int:pk>/', UserDeleteView.as_view()),
]