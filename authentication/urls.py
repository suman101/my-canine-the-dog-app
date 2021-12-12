from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterApi, LogoutView,  ChangePasswordView, RequestPasswordResetEmail, PasswordTokenCheckAPI, SetNewPasswordAPIView, GoogleLogin, ProfileCreateView, ProfileDetailView, ProfileDeleteView


urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/register/', RegisterApi.as_view()),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
    
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    
    path('profile/', ProfileCreateView.as_view()),
    path('profile-detail/<int:pk>/', ProfileDetailView.as_view()),
    path('profile-delete<int:pk>/', ProfileDeleteView.as_view()),
]